#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
import dqlib.proto.dqlib_pb2 as dqlib_pb2
import dqlib.proto.dqlib_pb2_grpc as dqlib_pb2_grpc
from dotenv import load_dotenv
import os


def process_request(service_name, pb_input_bin):
    load_dotenv()
    _HOST = os.getenv("HOST", "127.0.0.1")
    _PORT = os.getenv("PORT", "50052")
    print(_HOST)
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = dqlib_pb2_grpc.DqlibServiceStub(channel=conn)
    response = client.RemoteCall(dqlib_pb2.DqlibRequest(name=service_name, serialized_request=pb_input_bin))
    if response.serialized_response == None:
        raise Exception('DqlibRequest: failed!')
    return response.serialized_response
