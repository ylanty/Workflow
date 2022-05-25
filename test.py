import func

def test(test):
    try:
        func.daylylog(test)
    except Exception as e:
        print("xiaoaishe有错误:", e)

    
if __name__ == '__main__':
    # 
    func.daylylog('123')
