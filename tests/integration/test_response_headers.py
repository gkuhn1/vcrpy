# coding=utf-8
"""Test basic functionalityes of VCRHttpResponse"""

from vcr.stubs import VCRHTTPResponse

def test_getheader(tmpdir):
    recorded_response = {
        'body': {'string': ''},
        'status': {'code': 404, 'message': 'Not Found'},
        'headers': ["x-amz-request-id: FADCBA44C48A5B9B\r\n", "x-amz-id-2: fgclTdyPxGwYJzNT1guOeaEJBWgStidAcDtRK77O+njKHgmRbzKUUfGxmi/a2BEY\r\n",
            "Content-Type: application/xml\r\n", "Transfer-Encoding: chunked\r\n", "Date: Wed, 05 Feb 2014 14:02:32 GMT\r\n", "Server: AmazonS3\r\n"]
    }
    response = VCRHTTPResponse(recorded_response)
    assert response.getheader('Content-Type') == 'application/xml'

def test_getheader_upper_header(tmpdir):
    recorded_response = {
        'body': {'string': ''},
        'status': {'code': 404, 'message': 'Not Found'},
        'headers': ["Content-Type: application/xml\r\n", "Transfer-Encoding: chunked\r\n",
            "Date: Wed, 05 Feb 2014 14:02:32 GMT\r\n", "Location: http://www.testwebserver.com/404\r\n"]
    }
    response = VCRHTTPResponse(recorded_response)
    assert response.getheader('location') == 'http://www.testwebserver.com/404'

def test_getheader_with_default(tmpdir):
    recorded_response = {
        'body': {'string': ''},
        'status': {'code': 404, 'message': 'Not Found'},
        'headers': ["x-amz-request-id: FADCBA44C48A5B9B\r\n", "x-amz-id-2: fgclTdyPxGwYJzNT1guOeaEJBWgStidAcDtRK77O+njKHgmRbzKUUfGxmi/a2BEY\r\n",
            "Content-Type: application/xml\r\n", "Transfer-Encoding: chunked\r\n", "Date: Wed, 05 Feb 2014 14:02:32 GMT\r\n", "Server: AmazonS3\r\n"]
    }
    response = VCRHTTPResponse(recorded_response)
    assert response.getheader('location', 'http://default-location') == 'http://default-location'
