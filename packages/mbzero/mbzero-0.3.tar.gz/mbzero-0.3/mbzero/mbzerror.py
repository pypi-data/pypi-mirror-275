#  SPDX-FileCopyrightText: 2024 Louis Rannou
#
#  SPDX-License-Identifier: BSD-2


class MbzError(Exception):
    """Base class for all exceptions related to MusicBrainz."""
    pass


class MbzWebServiceError(MbzError):
    """Error related to MusicBrainz API requests."""
    def __init__(self, message=None, cause=None):
        """Pass ``cause`` if this exception was caused by another exception.
        """
        self.message = message
        self.cause = cause

    def __str__(self):
        if self.message:
            msg = "%s, " % self.message
        else:
            msg = ""
        msg += "caused by: %s" % str(self.cause)
        return msg


class MbzOauth2Error(MbzWebServiceError):
    """OAuth2 failure"""
    pass
