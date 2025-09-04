def count_notes(m):
    notes=[2000,500,200,100,50,20,10,5,2,1]
    note_count={}
    for note in notes:
        if m>=note:
            note_count[note]=m//note
            m=m%note
    return note_count
amount=int(input("enter amount"))
res=count_notes(amount)
for note,count in res.items():
    print(f"{note} : {count}")
    