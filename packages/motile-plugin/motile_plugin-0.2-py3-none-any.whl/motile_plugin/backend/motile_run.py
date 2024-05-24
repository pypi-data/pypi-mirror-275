import json
from datetime import datetime
from pathlib import Path

import networkx as nx
import numpy as np
from pydantic import BaseModel

from .solver_params import SolverParams

STAMP_FORMAT = "%m%d%Y_%H%M%S"
PARAMS_FILENAME = "solver_params.json"
IN_SEG_FILEANME = "input_segmentation.npy"
OUT_SEG_FILEANME = "output_segmentation.npy"
TRACKS_FILENAME = "tracks.json"
GAPS_FILENAME = "gaps.txt"


class MotileRun(BaseModel):
    """An object representing a motile tracking run."""

    run_name: str
    solver_params: SolverParams
    input_segmentation: np.ndarray | None = None
    output_segmentation: np.ndarray | None = None
    tracks: nx.DiGraph | None = None
    time: datetime = datetime.now()
    gaps: list[float] = []
    status: str = "done"
    # pydantic does not check numpy arrays
    model_config = {"arbitrary_types_allowed": True}

    @staticmethod
    def _make_directory(time, run_name):
        stamp = time.strftime(STAMP_FORMAT)
        return f"{stamp}_{run_name}"

    @staticmethod
    def _unpack_directory(directory):
        stamp_len = len(datetime.now().strftime(STAMP_FORMAT))
        stamp = directory[0:stamp_len]
        run_name = directory[stamp_len + 1 :]
        try:
            time = datetime.strptime(stamp, STAMP_FORMAT)
        except ValueError as e:
            raise ValueError(
                f"Cannot unpack directory {directory} into timestamp and run name."
            ) from e
        return time, run_name

    def save(self, base_path: str | Path):
        base_path = Path(base_path)
        run_dir = base_path / self._make_directory(self.time, self.run_name)
        Path.mkdir(run_dir)
        self._save_params(run_dir)
        self._save_segmentation(
            run_dir, IN_SEG_FILEANME, self.input_segmentation
        )
        self._save_segmentation(
            run_dir, OUT_SEG_FILEANME, self.output_segmentation
        )
        self._save_tracks(run_dir)
        if self.gaps is not None:
            self._save_gaps(run_dir)

    @classmethod
    def load(cls, run_dir: Path | str):
        if isinstance(run_dir, str):
            run_dir = Path(run_dir)
        time, run_name = cls._unpack_directory(run_dir.stem)
        params = cls._load_params(run_dir)
        input_segmentation = cls._load_segmentation(run_dir, IN_SEG_FILEANME)
        output_segmentation = cls._load_segmentation(run_dir, OUT_SEG_FILEANME)
        tracks = cls._load_tracks(run_dir)
        gaps = cls._load_gaps(run_dir)
        return cls(
            run_name=run_name,
            solver_params=params,
            input_segmentation=input_segmentation,
            output_segmentation=output_segmentation,
            tracks=tracks,
            time=time,
            gaps=gaps,
        )

    def _save_params(self, run_dir):
        params_file = run_dir / PARAMS_FILENAME
        with open(params_file, "w") as f:
            json.dump(self.solver_params.__dict__, f)

    @staticmethod
    def _load_params(run_dir: Path) -> SolverParams:
        params_file = run_dir / PARAMS_FILENAME
        if not params_file.is_file():
            raise FileNotFoundError(f"Parameters not found at {params_file}")
        with open(params_file) as f:
            params_dict = json.load(f)
        return SolverParams(**params_dict)

    def _save_segmentation(self, run_dir, seg_file, segmentation):
        seg_file = run_dir / seg_file
        np.save(seg_file, segmentation)

    @staticmethod
    def _load_segmentation(
        run_dir: Path, seg_file: str, required: bool = True
    ) -> np.ndarray:
        seg_file = run_dir / seg_file
        if seg_file.is_file():
            return np.load(seg_file)
        elif required:
            raise FileNotFoundError(f"No segmentation at {seg_file}")
        else:
            return None

    def _save_tracks(self, run_dir: Path):
        tracks_file = run_dir / TRACKS_FILENAME
        with open(tracks_file, "w") as f:
            json.dump(nx.node_link_data(self.tracks), f)

    @staticmethod
    def _load_tracks(run_dir: Path, required: bool = True) -> nx.DiGraph:
        tracks_file: Path = run_dir / TRACKS_FILENAME
        if tracks_file.is_file():
            with open(tracks_file) as f:
                json_graph = json.load(f)
            return nx.node_link_graph(json_graph, directed=True)
        elif required:
            raise FileNotFoundError(f"No tracks at {tracks_file}")
        else:
            return None

    def _save_gaps(self, run_dir: Path):
        gaps_file = run_dir / GAPS_FILENAME
        with open(gaps_file, "w") as f:
            f.write(",".join(map(str, self.gaps)))

    @staticmethod
    def _load_gaps(run_dir, required: bool = True) -> list[float]:
        gaps_file = run_dir / GAPS_FILENAME
        if gaps_file.is_file():
            with open(gaps_file) as f:
                gaps = list(map(float, f.read().split(",")))
            return gaps
        elif required:
            raise FileNotFoundError(f"No gaps found at {gaps_file}")
        else:
            return None

    def delete(self, base_path: str | Path):
        base_path = Path(base_path)
        run_dir = base_path / self._make_directory(self.time, self.run_name)
        # Lets be safe and remove the expected files and then the directory
        (run_dir / PARAMS_FILENAME).unlink()
        (run_dir / IN_SEG_FILEANME).unlink()
        (run_dir / OUT_SEG_FILEANME).unlink()
        (run_dir / TRACKS_FILENAME).unlink()
        (run_dir / GAPS_FILENAME).unlink()
        run_dir.rmdir()
