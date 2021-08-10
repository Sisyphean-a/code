import PySimpleGUI as sg

    
layout=[

[sg.Text("请输入你的信息")],
[sg.Text("姓名"),sg.InputText()],
[sg.Text("性别"),sg.InputText()],
[sg.Text("年龄"),sg.InputText()],
[sg.Text("种族"),sg.InputText()],
[sg.Button("确认"),sg.Button("取消")]
        ]


window=sg.Window("信息征集",layout)

while True:
    event,values=window.read()
    #print(event,values)
    if event=="确认":
        #sg.Popup(event,values)
        print(values[0])



    if event==None:
        break

window.close()

24215
53142