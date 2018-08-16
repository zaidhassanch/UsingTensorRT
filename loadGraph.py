# In my experience one of the two lines works
# Will add try/exception in the near future so that which ever line is required runs.
def getGraphDef(file, flag):
    with gfile.FastGFile(file,'rb') as f:
        if flag:
            graph_def.ParseFromString(f.read())
        else:
            text_format.Merge(f.read(), graph_def)
    return graph_def
