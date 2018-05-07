
def load_source(student, source_file):
    init = __import__(student)
    return init