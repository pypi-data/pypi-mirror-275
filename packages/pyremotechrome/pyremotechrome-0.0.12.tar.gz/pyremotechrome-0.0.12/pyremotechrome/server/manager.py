# Copyright (c) 2024 Wes-KW
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from inspect import signature
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pyremotechrome.config import Conf
from pyremotechrome.session import MegaBase
from pyremotechrome.session.support.common import Directory
from pyremotechrome.session.support.common import Vector
from pyremotechrome.session.support.common import Result
from pyremotechrome.session.support.options import FFMpegOptions
from pyremotechrome.util import print_exception
from pyremotechrome.util import get_value_in_dict
from pyremotechrome.util import filter_rules

# load the following from config.json
c = Conf()

# Session
session = c.session
size = session.size
__DEFAULT_WIDTH__ = size.window.width
__DEFAULT_HEIGHT__ = size.window.height
__SCREEN_WIDTH__ = size.screen.width
__SCREEN_HEIGHT__ = size.screen.height
__DEFAULT_SCALE__ = size.scale
__DATA_DIR__ = session.data_dir
__DEFAULT_URL__ = session.default_url
__USER_AGENT__ = session.user_agent
__WEBDRIVER_EXEC__ = session.webdriver_executable_path
__ACTION_ALLOW_RULES__ = session.rules.action.allow
__ACTION_DENY_RULES__ = session.rules.action.deny
__URL_ALLOW_RULES__ = session.rules.url.allow
__URL_DENY_RULES__ = session.rules.url.deny

# FFMpeg
ffmpeg = c.ffmpeg
__FFMPEG_EXEC__ = ffmpeg.ffmpeg_exec
__PROBESIZE__ = ffmpeg.probesize
__SEGMENT_TIME__ = ffmpeg.segment_time
__FRAME_PER_SEC__ = ffmpeg.frame_per_second
__QUEUE_SIZE_MULTIPLIER__ = ffmpeg.queue_size_multiplier
__AUDIO_ITSOFFSET__ = ffmpeg.audio_itsoffset
__MAXRATE__ = ffmpeg.maxrate
__BUFSIZE__ = ffmpeg.bufsize
__CRF__ = ffmpeg.constant_rate_factor

# Server
server = c.server
url = server.url
__WAVE_URL__ = f"{url.scheme}://{url.name}:{url.port}/wave/"
__DEBUG__ = server.debug


class RemoteSession(MegaBase):

    def __init__(self, id: str, user_agent: str = __USER_AGENT__) -> None:

        super().__init__(
            id=id,
            scale=__DEFAULT_SCALE__,
            data_dir=f"{__DATA_DIR__}/{id}",
            default_url=__DEFAULT_URL__,
            size=Vector(__DEFAULT_WIDTH__, __DEFAULT_HEIGHT__),
            screen_size=Vector(__SCREEN_WIDTH__, __SCREEN_HEIGHT__),
            wave_url=__WAVE_URL__,
            user_agent=user_agent,
            webdriver_exec=__WEBDRIVER_EXEC__,
            ffmpeg_options=FFMpegOptions(
                ffmpeg_exec=__FFMPEG_EXEC__,
                probesize=__PROBESIZE__,
                segment_time=__SEGMENT_TIME__,
                frame_per_second=__FRAME_PER_SEC__,
                queue_size_multiplier=__QUEUE_SIZE_MULTIPLIER__,
                audio_itsoffset=__AUDIO_ITSOFFSET__,
                maxrate=__MAXRATE__,
                bufsize=__BUFSIZE__,
                constant_rate_factor=__CRF__
            ),
            allow_rules=__URL_ALLOW_RULES__,
            deny_rules=__URL_DENY_RULES__
        )

class Manager:
    """Manage Remote Sessions"""

    _sessions: dict[str, RemoteSession]
    _data_dir: dict[str, str]

    def __init__(self) -> None:
        """DOCTSTRING"""
        self._sessions = {}
        self._data_dir = Directory(__DATA_DIR__)

    def create_session(self, session_id: str) -> Result:
        """
        If the Remote Session is not created, create a Remote Session and
        store it in an array. Then return a Result object with
        the first window_handle.
        """

        if session_id not in self._sessions:
            self._sessions[session_id] = RemoteSession(session_id)
            window_handle = self._sessions[session_id].get_current_window_handle()
            return Result(True, "", {"window_handle": window_handle})
        else:
            return Result(False, f"session `{session_id}` already exists.")

    def get_session_info(self, session_id: str) -> Result:
        """Return Session Result containing window_handles, _title and _icon"""

        if session_id in self._sessions:
            title = self._sessions[session_id].get_title()
            icon = self._sessions[session_id].get_icon()
            all_handles = self._sessions[session_id].get_window_handles()
            spec_handles = self._sessions[session_id].spec_handles
            handles = list(set(all_handles).difference(set(spec_handles)))
            res = {"title": title, "icon": icon, "handles": handles, "spec_handles": spec_handles}
            return Result(True, "", res)
        else:
            return Result(False, f"session `{session_id}` doesn't exists.")

    def destroy_session(self, session_id: str) -> Result:
        """DOCSTRING"""
        if session_id in self._sessions:
            self._sessions[session_id].quit()
            self._sessions.pop(session_id)
            return Result(True)
        else:
            return Result(False, f"session `{session_id}` doesn't exist.")

    def _call_from_url(self, url: str) -> Result:
        """DOCSTRING"""
        query = parse_qs(urlparse(url).query)
        if "request" not in query or query["request"][0] != "pyapi":
            return Result(False, "INVALID_API_REQUEST")

        action = get_value_in_dict(query, "action")
        session_id = get_value_in_dict(query, "session_id")
        if session_id is None:
            print_exception("EMPTY_SESSION_ID")
            return Result(False, "EMPTY_SESSION_ID")
        elif action is None:
            print_exception("EMPTY_API_ACTION")
            return Result(False, "EMPTY_API_ACTION")
        else:
            action = action[0]
            try:
                filter_rules(action, __ACTION_ALLOW_RULES__, __ACTION_DENY_RULES__)
            except Exception:
                print_exception("DENIED_API_ACTION")
                return Result(False, "DENIED_API_ACTION")

            session_id = session_id[0]
            if session_id not in self._sessions:
                print_exception("INVALID_SESSION_ID")
                return Result(False, "INVALID_SESSION_ID")

            sess = self._sessions[session_id]
            func = getattr(sess, action, None)
            if not callable(func):
                print_exception("INVALID_API_ACTION")
                return Result(False, "INVALID_API_ACTION")
            else:
                arguments = list(signature(func).parameters.keys())[1:]
                for argument in arguments:
                    if argument not in query:
                        print_exception("INVALID_API_ACTION_PARAMETERS")
                        return Result(False, "INVALID_API_ACTION_PARAMETERS")

                query.pop("request")
                query.pop("action")
                for q in query:
                    query[q] = query[q][0]

                res = func(**query)
                return Result(True, "" , res)

    def call_from_url(self, url: str) -> Result:
        """DOCSTRING"""
        try:
            return self._call_from_url(url)
        except Exception as e:
            if __DEBUG__:
               raise e
 
            print_exception(e)
            return Result(False, "INTERNAL_ERROR")
