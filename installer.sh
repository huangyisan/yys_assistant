#!/bin/bash
fbs clean && fbs freeze && cp ./src/main/python/config.ini target/yys_assistant/ && cp ./src/main/python/alipay_qrcode.png target/yys_assistant/ && fbs installer
