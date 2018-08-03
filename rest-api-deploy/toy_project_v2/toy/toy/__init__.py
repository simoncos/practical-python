#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, Response
import json
import traceback

from toy.module_a.logic import cut
from toy.utils.exception import *
from toy.utils.logger import LoggerFactory
from toy.utils.timer import Timer

app = Flask(__name__) # create a Flask instance

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/cut/para/<string:content>') # syntax warning: must not have space beside ":"
def paraCut(content):
    word_str, word_num = cut(content)
    return "words: {}; number of words: {}".format(word_str, word_num)

@app.route('/cut/json', methods=['POST'])
def jsonCut():

    log = LoggerFactory.getDebugLogger()

    status = None
    message = None
    output_data = {}
    docid = None

    try:
        # get JSON in the request
        json_dict = request.get_json()
        log.info('Processing starts, input: {}'.format(json_dict))
        # check input
        docid = json_dict['docid']
        content = json_dict['content']
        extra = json_dict.get('extra', None)
        if content == '':
            raise EmptyContentException('Content is empty')
        if extra is None:
            log.warning('docid:{}, API Internal Warn: '.format(docid) + 'Missing attribute "extra"')

        # run business logic
        with Timer() as t:
            word_str, word_num = cut(content, docid)
        log.info("docid:{}, Processing time for cut is: {}".format(docid, t.elapse))

        # prepare Response info
        output_data = {'word_str': word_str, 'word_num': word_num}
        status = ErrorCode.SUCCESS.value
        message = 'OK'

    except Exception as e:
        if type(e) not in TRACKED_EXCEPTIONS:
            status = ErrorCode.ERROR.value
            log_level = 'error'
        else:
            status = e.code.value
            log_level = e.log_level
        message = '{}: {}'.format(type(e).__name__, str(e))

        if log_level == 'error':
            log.error('docid:{}, API Internal Error:\n'.format(docid) + str(traceback.format_exc()))
        elif log_level == 'warning':
            log.warning('docid:{}, API Internal Warn: '.format(docid) + str(message))

    finally:
        output = {'message': message, 'data': output_data}
        js = json.dumps(output)
        response = Response(js, status=status, mimetype='application/json')
        log.info("docid:{}, Processing finished, result is: {}".format(docid, output))
        return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
