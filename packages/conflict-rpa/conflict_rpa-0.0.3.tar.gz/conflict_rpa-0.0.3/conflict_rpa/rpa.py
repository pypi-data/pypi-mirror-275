import argparse
import os
from conflict_rpa.config import read_all_config, init_config

openai_config = read_all_config()
if openai_config is None:
    print('需要初始化OPENAI配置')
    init_config()


def rpa():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', type=str, help="提供链接进行自动化操作", default=None)
    parser.add_argument('-t', '--tutorial', type=str, help="希望自动化操作的流程文本，不需要整理地很好", default=None)
    parser.add_argument('command',
                        nargs='*',
                        help='希望自动化执行的命令行指令，默认为同上一条执行的指令；也可以是自然语言')
    args = parser.parse_args()
    openai_config = read_all_config()
    if openai_config is None:
        print('需要初始化OPENAI配置')
        init_config()
        return
    else:
        OPENAI_API_KEY = openai_config["OPENAI_API_KEY"]
        OPENAI_API_BASE = openai_config["OPENAI_API_BASE"]
        os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
        if len(OPENAI_API_BASE):
            os.environ['OPENAI_API_BASE'] = OPENAI_API_BASE
    from conflict_rpa.content_rpa import content_rpa
    from conflict_rpa.correcting_framework import main_loop
    from conflict_rpa.link_rpa import link_rpa
    if args.link:
        print(f"正在处理链接: {args.link}")
        # 在这里添加处理链接的代码
        link_rpa(args.link)
    elif args.tutorial:
        print(f"正在处理文本: {args.tutorial}")
        # 在这里添加处理链接的代码
        content_rpa(args.tutorial)
    else:
        if len(args.command) == 1:
            history_cmd = args.command[0]
        elif len(args.command) > 1:
            history_cmd = ''.join(args.command[1:])
        else:
            print('没有可执行的指令')
            return
        print(f"运行指令 {history_cmd}")
        script = ''.join(history_cmd).replace('\t', '')
        main_loop(script)
