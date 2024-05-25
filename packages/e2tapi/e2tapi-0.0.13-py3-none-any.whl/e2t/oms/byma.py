import socket
import threading
import random
import string
from google.protobuf.message import DecodeError
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
from abc import abstractmethod

from e2t.oms import BYMA_Messages_pb2 as pb


class BYMA_OMS:

    @abstractmethod
    def status(self, clOrdID, orderID, quantity, price, live, cumQty, leavesQty, avgPx, lastPx):
        pass

    @abstractmethod
    def reject(self, idRef, reason):
        pass

    @abstractmethod
    def trade(self, orderId, execId, time, lastQty, lastPx, avgPx, cumQty):
        pass

    def connect(self, HOST, PORT):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))

        print(f"Conectado a {HOST}:{PORT}...")

        self.send_token_req("666", 'clientID')
        def handle_client():
            while True:
                try:
                    data = self.client.recv(1024)
                    if not data:
                        break
                    message = pb.Message()
                    size, new_pos = _DecodeVarint32(data, 0)
                    message.ParseFromString(data[new_pos:new_pos + size])

                    if message.messageType == pb.MessageType.ORDER_STATUS:
                        self.status(
                            message.orderStatus.clOrdID,
                            message.orderStatus.orderID,
                            message.orderStatus.quantity,
                            message.orderStatus.price,
                            message.orderStatus.live,
                            message.orderStatus.cumQty,
                            message.orderStatus.leavesQty,
                            message.orderStatus.avgPx,
                            message.orderStatus.lastPx
                        )
                    elif message.messageType == pb.MessageType.TRADE_ORDER:
                        self.trade(
                            message.tradeOrder.orderId,
                            message.tradeOrder.execId,
                            message.tradeOrder.time,
                            message.tradeOrder.lastQty,
                            message.tradeOrder.lastPx,
                            message.tradeOrder.avgPx,
                            message.tradeOrder.cumQty
                        )
                    elif message.messageType == pb.MessageType.REJECT:
                        self.reject(
                            message.reject.idRef,
                            message.reject.reason
                        )
                    elif message.messageType == pb.MessageType.TOKEN_RESPONSE:
                        self.token = message.tokenResponse.token
                    else:
                        print(f"Unknown message type: {message.messageType}")
                except DecodeError as e:
                    print(f"Error decoding message: {e}")
                    break

        threading.Thread(target=handle_client, daemon=True).start()

    def send_order(self, order_buffer):
        if self.client:
            size = len(order_buffer)
            self.client.sendall(_VarintBytes(size) + order_buffer)
        else:
            print("Error: Cliente no disponible para el usuario")

    def send_token_req(self, clientID, busID):
        token_request = pb.TokenRequest(
            clientID=str(clientID),
            busID=busID
        )
        message = pb.Message(
            messageType=pb.MessageType.TOKEN_REQUEST,
            tokenRequest=token_request
        )
        buffer = message.SerializeToString()
        self.send_order(buffer)

    def send_limit_order(self, side, securityID, quantity, price, timeInForce, expireTime, settlType, account,
                          display):
        limit_order = pb.LimitOrder(
            token=self.token,
            clOrdID=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            side=side,
            securityID=securityID,
            quantity=quantity,
            price=price,
            timeInForce=timeInForce,
            expireTime=expireTime,
            settlType=settlType,
            account=account,
            display=display
        )
        message = pb.Message(
            messageType=pb.MessageType.LIMIT_ORDER,
            limitOrder=limit_order
        )
        buffer = message.SerializeToString()
        self.send_order(buffer)

    def send_limit_replace(self, origClOrdID, quantity, price, expireTime, account, display):
        limit_replace = pb.LimitReplace(
            token=self.token,
            clOrdID=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            origClOrdID=origClOrdID,
            quantity=quantity,
            price=price,
            expireTime=expireTime,
            account=account,
            display=display
        )
        message = pb.Message(
            messageType=pb.MessageType.LIMIT_REPLACE,
            limitReplace=limit_replace
        )
        buffer = message.SerializeToString()
        self.send_order(buffer)

    def send_limit_cancel(self, origClOrdID):
        limit_cancel = pb.LimitCancel(
            token=self.token,
            clOrdID=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)),
            origClOrdID=origClOrdID
        )
        message = pb.Message(
            messageType=pb.MessageType.LIMIT_CANCEL,
            limitCancel=limit_cancel
        )
        buffer = message.SerializeToString()
        self.send_order(buffer)
