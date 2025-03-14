__import__('os').rename("compilepyx.ss", "compilepyx.py")
__import__('subpr').lib.run("python -m subpr.compile compilepyx.py")