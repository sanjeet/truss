import signal
from typing import Any, List, Optional

from truss.cli.logs.base_watcher import LogWatcher
from truss.cli.train.poller import TrainingPollerMixin
from truss.cli.utils.output import console
from truss.remote.baseten.api import BasetenApi


class TrainingLogWatcher(TrainingPollerMixin, LogWatcher):
    project_id: str
    job_id: str

    def __init__(self, api: BasetenApi, project_id: str, job_id: str):
        TrainingPollerMixin.__init__(self, api, project_id, job_id)
        LogWatcher.__init__(self, api)
        # registering the sigint allows us to provide messaging on next steps
        signal.signal(signal.SIGINT, self._handle_sigint)

    def _handle_sigint(self, signum: int, frame: Any) -> None:
        msg = f"\n\nExiting training job logs. To stop the job, run `truss train stop --job-id {self.job_id}`"
        console.print(msg, style="yellow")
        raise KeyboardInterrupt()

    def fetch_logs(
        self, start_epoch_millis: Optional[int], end_epoch_millis: Optional[int]
    ) -> List[Any]:
        return self.api.get_training_job_logs(
            self.project_id, self.job_id, start_epoch_millis, end_epoch_millis
        )
