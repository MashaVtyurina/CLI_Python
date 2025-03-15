import argparse
from send import send_msg
from logging import LOGGER


def parse_args():
    parser = argparse.ArgumentParser(description='CLI for sending messages')
    parser.add_argument('sender', help='Sender:')
    parser.add_argument('recipient', help='Receiver:')
    parser.add_argument('msg', help='Message')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    LOGGER.info(f' {args.sender} has just sent to {args.recipient} message: {args.msg}')
    response = send_msg(args.sender, args.recipient, args.msg)
    LOGGER.info(f'Client received a this server-response: {response}')
    print(response)
