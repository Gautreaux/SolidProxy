
from SolidProxy.bootstrap import GetOrStartSWInst

if __name__ == "__main__":
    sw_inst = GetOrStartSWInst()
    assert(sw_inst is not None)


    open_docs = sw_inst.GetDocuments()

    print(f"There are {len(open_docs)} open documents:")
    
    for doc in open_docs:
        print(" [{}]<{}> {} ({})".format(
            ("R " if doc.IsOpenedReadOnly() else "RW"),
            doc.GetType().what(), doc.GetTitle(),
            doc.GetPathName(),
        ))
