
def used_function():
    return True

def unused_function():
    return False

class SampleClass:
    def used_method(self):
        return used_function()
        
    def unused_method(self):
        return unused_function()

def main():
    sample = SampleClass()
    return sample.used_method()

if __name__ == "__main__":
    main()