#  SPDX-FileCopyrightText: 2024 Louis Rannou
#
#  SPDX-License-Identifier: BSD-2

import unittest

from mbzero import mbzerror as mbe


class ErrorTest(unittest.TestCase):
    def testMbzError(self):
        t = False
        try:
            raise mbe.MbzError
        except mbe.MbzError:
            t = True
        self.assertTrue(t)

    def testMbzWebServiceError(self):
        t = False
        try:
            raise mbe.MbzWebServiceError("hello")
        except mbe.MbzWebServiceError:
            t = True
        self.assertTrue(t)

    def testMbzWebServiceErrorMessage(self):
        info = "errorinfo"
        t = False
        try:
            raise mbe.MbzWebServiceError(info)
        except mbe.MbzWebServiceError as e:
            import io
            s = io.StringIO()
            print(e, file=s)
            self.assertEqual(
                s.getvalue().strip(), info + ", caused by: None"
            )
            t = True
        self.assertTrue(t)

    def testMbzWebServiceErrorCause(self):
        info = "errorinfo"
        t = False
        try:
            raise mbe.MbzWebServiceError(None, info)
        except mbe.MbzWebServiceError as e:
            import io
            s = io.StringIO()
            print(e, file=s)
            self.assertEqual(
                s.getvalue().strip(), "caused by: " + info
            )
            t = True
        self.assertTrue(t)

    def testMbzOauth2Error(self):
        t = False
        try:
            raise mbe.MbzOauth2Error
        except mbe.MbzOauth2Error:
            t = True
        self.assertTrue(t)
