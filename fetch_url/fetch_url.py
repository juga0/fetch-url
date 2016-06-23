"""fetch_url."""
from nameko.web.handlers import http
from werkzeug.wrappers import Response
from werkzeug import exceptions
import json

class FetchURLService(object):
    name = "fetchurl"

    # @http('GET', '/privileged')
    # def forbidden(self, request):
    #     return 403, "Forbidden"
    #
    # @http('GET', '/headers')
    # def redirect(self, request):
    #     return 201, {'Location': 'https://www.example.com/widget/1'}, ""

    @http('GET', '/fetchurl/<string:url>/<string:etag>/<string:last_modified>')
    def fetch_url(self, request, url, etag, last_modified):
        """
        /a/v/t is for entity/attribute/value/transaction
        {
          e: "https://guardianproject.info/home/data-usage-and-protection-policies/",
          a: "etag",
          v: E43A29F57...,
          t: {
              id: "watch-url",
              agent: $AGENT_ID,
              timestamp: $AGENT_TIMESTAMP
          }
        }
        """
        if request.method != "GET":
          raise exceptions.MethodNotAllowed
        # TODO: get url from website, returning this for now
        return Response(json.dumps({'url': url, 'etag': etag}))
        # ismodified, content, headers = get_ismodified(url, etag_db, last_modified_db)


    @http('POST', '/post')
    def do_post(self, request):
        if request.method != "POST":
          raise exceptions.MethodNotAllowed
        return "received: {}".format(request.get_data(as_text=True))

    # if not request.content_type.startswith('application/json'):
    #   raise exceptions.BadRequest
    # try:
    #   data = json.loads(request.data)
    # except ValueError, e:
    #   resdata = {'jsonrpc':'2.0',
    #              'id':None,
    #              'error':{'code':PARSE_ERROR,
    #                       'message':errors[PARSE_ERROR]}}
    #
    # else:
    #   if isinstance(data, dict):
    #     resdata = self.process(data)
    #   elif isinstance(data, list):
    #     if len([x for x in data if not isinstance(x, dict)]):
    #       resdata = {'jsonrpc':'2.0',
    #                  'id':None,
    #                  'error':{'code':INVALID_REQUEST,
    #                           'message':errors[INVALID_REQUEST]}}
    #     else:
    #       resdata = [d for d in (self.process(d) for d in data)
    #                  if d is not None]
    #
    #
    # response = Response(content_type="application/json")
    #
    # if resdata:
    #   response.headers["Cache-Control"] = "no-cache"
    #   response.headers["Pragma"] = "no-cache"
    #   response.headers["Expires"] = "-1"
    #   response.data = json.dumps(resdata)
    # return response(environ, start_response)
