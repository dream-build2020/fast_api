from ansible_runner import run

result = run(private_data_dir='/data/')

# 获取任务的代码
return_code = result.rc

# 获取任务的输出
return_stdout = result.stdout

# 获取任务的错误信息
return_stderr = result.stderr
