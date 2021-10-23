# Flare-on-8: wizardcult
# Phân tích PCAP

Tại `tcp.stream eq 1` sẽ thấy được client cho tải xuống file `induct` vào `/mages_tower` từ địa chỉ `http/[wizardcult.flare-on.com](http://wizardcult.flare-on.com/)/induct`

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%201.png)

`tcp.stream eq 2` nôm na là binary của file induct.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%202.png)

`tcp.stream eq 3` sẽ thực hiện lệnh chmod cho file `induct` đã tải xuống

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%203.png)

`tcp.stream eq 4` thực thi file đó

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%204.png)

`tcp.stream eq 5` giống như là cuộc hội thoại của một game RPG.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%205.png)

`tcp.stream eq 6` i don't known it.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%206.png)

# Phân tích file

File sẽ được phần tích gồm 2 giai đoạn, giai đoạn 1 là từ đầu đến khi giết xong Goblin

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%207.png)

Đoạn 2 thì còn lại.

## Giai đoạn 1:

Sử dụng lumina trong ida pro để làm rõ tên hàm hơn.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%208.png)

Tại hàm `main_main` sử dụng chuỗi [`wizardcult.flare-on.com`](http://wizardcult.flare-on.com/) làm domain để kết nối, và những hàm github_com_lrstanley_girc cho biết rằng sẽ kết nối đến server `IRC` 

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%209.png)

Sau khi thực thi hàm `main_main` sẽ đến hàm `main_main_func1`, tại đây thấy được chương trình sau khi kết nối vào IRC sẽ join vào channel `dungeon`  

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2010.png)

Sau khi thực hiện kết nối, chương trình sẽ thực thi hàm `mapassign` cùng với các tham số được gán trước đó
(xem thêm về `mapassign`ở [https://x0r19x91.gitlab.io/reversing-golang/part-3/](https://x0r19x91.gitlab.io/reversing-golang/part-3/) )

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2011.png)

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2012.png)

Tạo một struct làm type cho các biến tương tự như `v25` để có thể rõ ràng hơn

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2013.png)

và sẽ thấy được có 2 hàm sử dụng: **ReadFile_Potion** và **Command_Potion**

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2014.png)

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2015.png)

Từ đây tôi có thể tóm gọn được rằng, sau khi client tải xuống, cấp quyền và thực thi file `induct` thì chương trình sẽ thực hiện việc kết nối IRC đến server có domain là [`wizardcult.flare-on.com`](http://wizardcult.flare-on.com/) sau đó sẽ join vào channel `#dungeon` , để có thể thực hiện được việc debug (tôi sử dụng `remote linux debugger` của IDA) thì cần phải cài đặt môi trường cho nó:

## Tại server

- Sử dụng UnrealIRCd

## Tại client

- Đặt `induct` vào đúng đường dẫn `/mages_tower`
- Gắn địa chỉ của domain vào ip của server trong file `/etc/hosts`
- DEBUG.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2016.png)

Từ hàm `main_main_func2` sẽ có kiểm tra user có tên `dung3onm4st3r13` có trong server không.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2017.png)

nếu có thì sẽ trải qua 1 loạt instruction và để ý tại hàm `wizardcult_comms_ProcessDMMessage` , hàm này sẽ xử lý các tin nhắn mà `dung3onm4st3r13` gửi lên server.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2018.png)

ở trong hàm `wizardcult_comms_ProcessDMMessage` có hàm `strings_index` dùng để lấy vị trí xuất hiện của chuỗi được gán trong tin nhắn gửi đến, nếu <0 thì có nghĩa là chuỗi được gán không có trong tin nhắn gửi đến. Sau khi điều kiện đúng sẽ thực hiện một loạt instruction nào đó và cuối cùng là send tin nhắn đến server IRC.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2019.png)

Và ở dưới cũng tương tự như thế.

Tại đoạn so sánh với chuỗi `you have learned how to create the` thì sẽ thấy sử dụng các chuỗi từ bảng `wizardcult_tables_Ingredients` để làm điều gì đó. Ngoài ra thì tại lúc này bên wireshark sẽ thầy IRC gửi rất nhiều như : "To brew it you must combine magnifying glass,.....". 

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2020.png)

Kết hợp với debug sẽ hiểu được rằng mỗi 2 từ được gửi đi kể từ sau "combine " chính là mỗi byte của binary data struct được sử dụng làm tham số truyền vào cho hàm `wizardcult_vm_LoadProgram`

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2021.png)

Độ dài của bảng này là 0x100

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2022.png)

Nên sử dụng python script để dump table ra file json

```python
import json

start_offset = 0x94B580
# end_offset =  0x94B8F0
size = 0x1000

shellcode = idaapi.get_bytes(start_offset, size)
hexList = list(shellcode)

arrList = []
for i in range(0, len(hexList), 8):
    temp = (hexList[i+7])&0xff
    temp = ((temp << 8) + hexList[i+6])&0xffff
    temp = ((temp << 8) + hexList[i+5])&0xffffff
    temp = ((temp << 8) + hexList[i+4])&0xffffffff
    temp = ((temp << 8) + hexList[i+3])&0xffffffffff
    temp = ((temp << 8) + hexList[i+2])&0xffffffffffff
    temp = ((temp << 8) + hexList[i+1])&0xffffffffffffff
    temp = ((temp << 8) + hexList[i])&0xffffffffffffffff
    arrList.append(temp)

result = []
id = 0
for i in range(0, len(arrList), 2):
    offset = arrList[i]
    length = arrList[i+1]
    text = idaapi.get_bytes(offset, length)
    result.append({
        'id': id,
        'offset': offset,
        'length': length,
        'text': text.decode("utf-8")
    })
    id = id+1
json_object = json.dumps(result, indent = 3)
with open("dump1.json", "w") as outfile:
    outfile.write(json_object)
```

Được file dump.json:

[dump1.json](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8cf1bccc-5f95-4366-ba14-bbf97c3d0d12/dump1.json)

Hàm `runtime_mapaccess2_faststr` sẽ trả về con trỏ đến hàm tương ứng với khóa là v87 trong `map` (map đã được khởi tạo ở hàm `main_main_func1` bởi các hàm `runtime_mapassign_faststr` , xem thêm chi tiết ở [https://x0r19x91.gitlab.io/reversing-golang/part-3/](https://x0r19x91.gitlab.io/reversing-golang/part-3/))

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2023.png)

Debug thì tôi thấy được key là "Potion of Acid Resistance."

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2024.png)

Thì tương đương nó sẽ lấy con trỏ đến hàm `Command_Potion` .

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2025.png)

Đặt breakpoint tại hàm `Command_Potion` 

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2026.png)

Quay lại hàm `wizardcult_comms_ProcessDMMessage`, hàm `runtime_mapaccess1_faststr` tương tự như hàm `runtime_mapaccess2_faststr` .

Hàm `wizardcult_vm_LoadProgram` sẽ bắt đầu load vm với binary data struct đã encode bởi GOB (v23)
(xem thêm [https://www.youtube.com/watch?v=SE13kcjJ_X0](https://www.youtube.com/watch?v=SE13kcjJ_X0) ) được `dung3onm4st3r13` gửi đến.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2027.png)

Debug và dump sẽ được binay truyền vào (hoặc có thể sử dụng file json đã dump ở trên và nội dung mà `dung3onm4st3r13`  gửi đến để tạo ra được binary đó).

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2028.png)

Trong hàm `wizardcult_vm_LoadProgram` decrypt đoạn binary trên và tạo vm.

![alt text](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2029.png)

Sử dụng degob ([https://github.com/drosseau/degob](https://github.com/drosseau/degob)) để decrypt đoạn binary trên thì được :

```go
// type ID: 67
type OutputDevice struct {
	Name string
}

// type ID: 68
type Cpu struct {
	Acc int64
	Dat int64
	Pc int64
	Cond int64
	Instructions []vm.Instruction
}

// type ID: 69
type Instruction struct {
	Opcode int64
	A0 int64
	A1 int64
	A2 int64
	Bm int64
	Cond int64
}

// type ID: 73
type []int []int64

// type ID: 76
type []vm.RAM []RAM

// type ID: 75
type RAM struct {
	A0 int64
	A1 int64
	Data []int
}

// type ID: 66
type InputDevice struct {
	Name string
}

// type ID: 72
type ROM struct {
	A0 int64
	A1 int64
	Data []int
}

// type ID: 77
type Link struct {
	LHDevice int64
	LHReg int64
	RHDevice int64
	RHReg int64
}

// type ID: 65
type Program struct {
	Magic int64
	Input InputDevice
	Output OutputDevice
	Cpus []vm.Cpu
	ROMs []vm.ROM
	RAMs []vm.RAM
	Links []vm.Link
}

// type ID: 71
type []vm.Cpu []Cpu

// type ID: 70
type []vm.Instruction []Instruction

// type ID: 74
type []vm.ROM []ROM

// type ID: 78
type []vm.Link []Link

Program
{
	Magic: 4919, 
	Input: InputDevice{Name: ""}, 
	Output: OutputDevice{Name: ""}, 
	Cpus: []Cpu{
			Cpu{Acc: 0, Dat: 0, Pc: 0, Cond: 0, 
				Instructions: []Instruction{
				Instruction{Opcode: 1, A0: 0, A1: 4, A2: 0, Bm: 3, Cond: 0}, 
				Instruction{Opcode: 5, A0: 4, A1: -1, A2: 0, Bm: 1, Cond: 0}, 
				Instruction{Opcode: 1, A0: -1, A1: 1, A2: 0, Bm: 2, Cond: 1}, 
				Instruction{Opcode: 1, A0: 0, A1: 4, A2: 0, Bm: 3, Cond: 1}, 
				Instruction{Opcode: 1, A0: 4, A1: 2, A2: 0, Bm: 3, Cond: 0}, 
				Instruction{Opcode: 1, A0: 2, A1: 4, A2: 0, Bm: 3, Cond: 0}, 
				Instruction{Opcode: 1, A0: 4, A1: 1, A2: 0, Bm: 3, Cond: 0}}}, 
			Cpu{Acc: 0, Dat: 0, Pc: 0, Cond: 0, 
				Instructions: []Instruction{
				Instruction{Opcode: 1, A0: 0, A1: 4, A2: 0, Bm: 3, Cond: 0}, 
				Instruction{Opcode: 18, A0: 162, A1: 0, A2: 0, Bm: 0, Cond: 0}, 
				Instruction{Opcode: 1, A0: 4, A1: 0, A2: 0, Bm: 3, Cond: 0}}}}, 
	ROMs: []ROM{}, 
	RAMs: []RAM{}, 
	Links: []Link{
			Link{LHDevice: 0, LHReg: 0, RHDevice: 2, RHReg: 0}, 
			Link{LHDevice: 2, LHReg: 1, RHDevice: 1, RHReg: 0}, 
			Link{LHDevice: 2, LHReg: 2, RHDevice: 3, RHReg: 0}}}
```

Sau khi load VM xong chương trình sẽ chạy một loạt instruction sau đó gửi tin nhắn lên server.

Từ đây có thể hiểu được  `dung3onm4st3r13` là đối tượng điều khiển luồng chạy của chương trình bằng tin nhắn gửi đến. Vì thế có con bot mang danh `dung3onm4st3r13` (made by @Hoàng Nguyễn Minh) như sau :

[replay.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6c56966f-afb2-4138-8770-4ad075b5c004/replay.py)

[ingre2.txt](https://github.com/konoha279/Flare-on-8/blob/main/image/Untitled%2030.png)

Theo luồng tin nhắn trong wireshark thì tiếp theo là đến if với "you enter the dungeon" (có thể debug để chắc chắn điều này). Tại đoạn này sẽ load table như ở phía trên kia để làm điều gì đó

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e6fd4b73-a64e-42fc-89a2-a5cdde5b0797/Untitled.png)

Dump table đó ra thì được:

[dump2.json](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/afb32d1d-4b77-4b78-bd15-0b94209e257e/dump2.json)

Sau đoạn đó sẽ đến đoạn if với "It stares at you imposingly."

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6a170330-8a60-40ab-a253-9e23311572b1/Untitled.png)

Tại đoạn này sẽ cần để ý đến hàm `wizardcult_comms_CastSpells` 

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/987d7605-804c-4982-af14-64b658b19727/Untitled.png)

Trong hàm đó sẽ có một table string nữa `wizardcult_tables_Spells`

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4ccfb3a3-242c-413f-98ec-0019597d02ed/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9fa5f6f9-6019-4555-b112-5300d3e25e8b/Untitled.png)

Dump ra được: 

[dump3.json](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9869948f-28b9-4da8-aeed-58e3e650fb8c/dump3.json)

Bây giờ sẽ dùng "Moonbeam" để tìm trong dump2.json và dump3.json

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7457f726-7ebc-4253-a17b-2e5f5f537d1c/Untitled.png)

thì thấy có xuất hiện ở dump3.json và có id là 193. 

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4171b5e-189b-49aa-ba66-00d64475a826/Untitled.png)

Để đấy.

Lúc này debug cho luồng chương trình chạy đến `wizardcult_potion_CommandPotion`

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7dbe14ab-d83e-4f92-b595-273879a2d522/Untitled.png)

và chạy đến dòng 42, sẽ thấy ở stack sẽ đưa tất cả tên file trong folder vào stack

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/83fc2699-7da9-45ab-8ffa-2423959a2d9d/Untitled.png)

theo dõi chương trình thì sẽ thầy hàm `wizardcult_vm__ptr_Cpu_Execute` , hàm này sẽ load vm và excute instruction bằng hàm `wizardcult_vm__ptr_Cpu_ExecuteInstruction` 

Kết hợp đống instruction từ file decrypt bằng degob và hàm `wizardcult_vm__ptr_Cpu_ExecuteInstruction` thì tôi thấy được các opcode sẽ qua switch để dùng instruction tương ứng. Như trong đoạn instruction đã decrypt thì lúc này chương trình chỉ có XOR với 162 và instruction Teq.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b034649-b8e4-48d4-a6ec-8a4bb0de643b/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f6c4bd6-ab11-4c32-a794-5aeae7d3a057/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a665d346-7f26-49a7-90f0-3f2304a825b1/Untitled.png)

Lúc này kết hợp với dump3,json với những điều trên cùng với đoạn chat này.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1cd0fa21-d80c-4b62-9772-072bc649c430/Untitled.png)

Thì tính toán ra được 2 tên file là `cool_wizard_meme.png` và `induct`

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14dc1ca5-5014-4d26-8143-c619935c7ef7/Untitled.png)

## Giai đoạn 2:

Từ giai đoạn 1 thì tôi biết được hướng đi là đúng.

Tiếp tục, tương tự những gì xảy ra ở giai đoạn 1 thì tại đoạn load vm, tôi lấy được binary data struct

[vm2.gob](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d55dcb50-5def-4d57-bea4-d58b04708e74/vm2.gob)

Dùng degob để decrypt thì nhận được

[vm2.txt](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/35eddc67-8115-4ea4-8157-5d61ac1cc2f3/vm2.txt)

Sau nhiều lần debug trâu bò thì biết được lúc này chương trình sẽ chạy hàm `wizardcult_potion_ReadFilePotion` , 

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fb283f6a-cd3c-4a9d-a645-9e69e44d665a/Untitled.png)

hàm này sẽ đọc toàn bộ byte của file `cool_wizard_meme.png`, sau đó toàn bộ byte đi qua thuật toán mã hóa của vm từ đó tạo ra các dòng tin nhắn từ các byte đã mã hóa và gửi lên IRC server.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1bf65ba3-7c9b-425b-979d-82079db83c49/Untitled.png)

Kết hợp với dump3.json lấy được file `cool_wizard_meme.png` đã bị mã hóa

[cool_wizard_meme.png.encrypted](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/160175cf-0cbf-41ec-8f7b-17c43a0c4d9c/cool_wizard_meme.png.encrypted)

Lúc này tôi sẽ tạo một binary fake của file để debug và đặt các breakpoint ở các instruction để lấy log

Chi tiết về đặt log thì đặt log tại mỗi call instruction, ví dụ như ở hàm `wizardcult_vm__ptr_Cpu_ExecuteMov` thì đặt bp tại call và thêm code như trong hình.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5eee8e9c-7268-4500-8293-fc6da2b0ed3e/Untitled.png)

Đi vào hàm thì đặt log ở những chỗ quan trọng. Tiếp tục ví dụ thì tôi đặt ở 2 nơi quan trọng.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/274b0c85-d971-43d0-9877-1143e3fa0214/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7c2afb49-30f4-41b8-88a3-70e13cf9ebbb/Untitled.png)

Cứ làm tương tự như ở các instruction còn lại tôi được 1 list breakpoint dùng để log

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/db455bc0-5e44-4a9c-b47a-bfdc71d097f4/Untitled.png)

File `cool_wizard_meme.png` thì cho nhị phân như trong hình (phần đầu là 8 byte signatures của file PNG sau đó toàn 'a'):

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8a673add-71b8-4563-ae33-72cebb5e144a/Untitled.png)

Sau khi debug thì tôi thu được đống log, từ lúc này kết hợp với [vm2.txt](https://www.notion.so/Write-up-wizardcult-8344f937999c4d6a9f1a52039c8ad3f9) thì bắt đầu chiêm nghiệm thuật  toán

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/83b24313-2611-4aed-8619-2ca8206d9a80/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/959b08ec-97fa-4d7a-92cc-3bfee1b32544/Untitled.png)

Tiến hành phần tích log, ở đoạn đầu thì thấy là `AND 0x01` và so sánh bằng 0x01.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6b35be5-e2be-4eb6-91c0-7337d47ff660/Untitled.png)

Thử tìm kiếm "& EAX:00000001h" thì thấy được sẽ con số sẽ tăng dần lên 1 đơn vị và AND với 0x01, thì có thể hiểu nôm na là index bắt đầu từ 0 và tăng dần mỗi 1 đơn vị, mỗi lần lặp như thế sẽ AND với 0x01 để kiểm tra tính chẵn lẽ.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48049048-ff7f-492f-8561-ba9c80fb8dd7/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c476a35a-d46c-4dfe-bbe7-ec89273f6c61/Untitled.png)

Ở lần index = 0 thì sẽ lấy byte 0x89 tương ứng với byte đầu tiên trong binary, sau đó so sánh lớn với 0x63 và trừ cho 0x64

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/66fb30f0-08fb-4f86-8fa3-aa400a5bb891/Untitled.png)

Bằng 1 phép màu nào đó 0x25 đã trở thành 0xB2 và XOR với 0x61

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7d2a1248-66ea-4629-929e-e308862e043f/Untitled.png)

Sau một lúc suy nghĩ thì lấy 0xB2 chuyển sang dạng thập phân là 178 sau đó tìm kiếm trong các data nằm trong vm2.txt đã decrypt được, thì thấy tại bảng thứ 2 tại vị trí 0x25 (37) có số 178. Mà để ý là tất cả phần tử của mảng 3 data đầu tiên là 255 và trước khi trừ đều có so sánh lớn với 99 (0x63)  nên tôi nghi vấn rằng byte từ 0 → 99 sẽ sử dụng data đầu tiên, 100→199 sử dụng data thứ 2, 200→ 255 sẽ sử dụng data thứ 3, đó chỉ mới là giả thuyết nên chưa chắc chắn.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5e049c4-75be-46d7-9ea6-35222b16fdb7/Untitled.png)

Sau khi có giá trị là 0xB2 thì tiếp tục XOR với 0x61 (97), và còn số này được lấy từ bảng data thứ 4 nên bảng thứ 4 là key (cũng là giả thuyết).

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8a50be4a-1758-468d-97ed-81e4584a215a/Untitled.png)

Sau khi XOR  xong được kết quả là 0xD3 và index cũng tăng lên 1. Tôi thấy 0xD3 được so sánh lớn 2 lần với 0x63 và 0xC7 sau đó trừ 0xC8, kết quả của phép trừ là 0xB

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4448a284-c785-4b57-b6ca-163a5d4a3dc5/Untitled.png)

Từ 0xB trở thành 0xED

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd652b85-17e7-4b63-a642-41acf477070c/Untitled.png)

Kiểm tra trong bảng data thứ 3 thì tại vị trí 0xB có được số 237 (0xED) ⇒ Giả thuyết đầu tiên khá chắc chắn 

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd5b256c-e233-4fec-a75d-ca381c4fe272/Untitled.png)

0x80 được AND với 0xED sau đó so sánh kết quả với 0x80 sau đó XOR với 0x42.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2aa9285-4302-40b8-bfa9-8cb131b95b6e/Untitled.png)

Tại khúc này tôi không hiểu vì sao 0xAF lại trở thành 0xFFFFFF50 có lẽ tôi đã đặt log thiếu ở đâu đó

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dbb4f85e-09de-433b-b14f-4838af594da7/Untitled.png)

Quay lại IDA và thấy được nơi tôi chưa đặt log. Vì thế thử lấy 0xAF ^ 0xFFFFFFFF thì thu được kết quả 0xFFFFFF50.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a63f707-dc40-41ce-9ebb-84691bc7b9a4/Untitled.png)

0xFFFFFF50 & 0xFFFFFFFF thì thu được 0x50, vậy là đã có byte được mã hóa đầu tiên, kiểm tra với file png bị mã hóa thì nhận ra có vẻ con đường đang đi là đúng đắng.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/81305309-b012-499f-a5bb-e2c7e92b1d61/Untitled.png)

Sau khi decrypt xong byte đầu tiên thì chương trình sẽ lấy byte tiếp theo để encrypt

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec0a2f36-1000-4d5d-9e1a-1d633686a5ff/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab11e8b3-fe10-4fcd-97d7-f9e1ebf3d458/Untitled.png)

Lúc này tôi sử dụng giả thuyết đầu tiên để tính byte 0x50 này thành byte bao nhiêu để xác nhận giả thuyết của tôi là đúng

Tính toán bằng giả thuyết tôi nhận được kết quả là 138 (0x8A)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f88172a3-b9f1-48d2-8704-818eec6271d0/Untitled.png)

Đọc bên log thì lấy 0x50 so sánh lớn với 0x63 nhưng không thỏa điều kiện nên giữ nguyên và được biến đổi thành 0x8A. Như vậy giả thuyết đầu tiên của tôi hoàn toàn đúng.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e3520f8-ac02-40cb-8325-ce18223e429a/Untitled.png)

Lúc này sẽ lấy 0x31 (49)  sau đó bằng 1 cách biến đổi nào đó trở thành 0xFFFFFFCE 

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33debd20-3d7a-4473-90c4-3723e7950cc3/Untitled.png)

Thì tôi thử dùng phép tính mà không log khi nãy tính 0x31 ^ 0xFFFFFFFF = 0xFFFFFFCE sau đó AND 0xFF thu được kết quả 0xCE. Sau đó XOR với 0x8A được kết quả 0x44

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd547030-3042-4812-ac72-fe3424f3a515/Untitled.png)

Tiếp theo là index tăng lên 1 và AND với 0x1 sau đó so sánh kết quả với 0x01.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b6044f25-1430-465b-a050-aa9173bd0894/Untitled.png)

0x44 được biến đổi thành 0xC9 (201)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2a1779c5-ba41-4439-865b-84e994b264ee/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b65e0de2-794d-4312-b6b2-3ca8ef2f1c59/Untitled.png)

0xC9 AND 0x80, lấy kết quả đi so sánh bằng với 0x80. Sau đó 0xC9 ^ 0x42 = 0x8B, 0x8B ^ 0xFFFFFFFF = 0xFFFFFF74, AND với 0xFF ta được 0x74, byte encrypt thứ 2.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a43d3211-fd0c-4344-90e3-ce2221799c1a/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/644fe1a9-4e9c-458a-84ba-21b92261deb3/Untitled.png)

Tiếp tục phân tích tương tự như trên cho byte thứ 3, đến khi AND 0x80 và có kết quả khác 0x80, thì ta thấy thay vì 0x62 XOR 0x42 sau đó XOR với 0xFFFFFFFF thì lần này sẽ lấy 0x62 XOR thẳng với 0xFFFFFFFF và  được byte encrypt là 0x9D.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f57a80ad-6d1f-489e-84ab-5761d295b831/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6e09750f-303e-4c25-80d5-b3dd21b0e67c/Untitled.png)

Ngoài ra thì tại lần encrypt byte thứ 3 thì cũng có XOR với 0x31.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c9d5d48f-3b5a-4379-801e-79d6a7598a3f/Untitled.png)

Để ý ở mỗi lần XOR, lần đầu tiên là 0x61 (97) lần thứ 2 thì là 0x31 (49) nhưng bị XOR với 0xFF, và lần thứ 3 là 0x31 (49). So sánh với bảng data thứ 4 thì có thể chắc chắn hơn rằng data thứ 4 là key để XOR nhưng mỗi lần lẻ thì key sẽ XOR với 0xFF.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88af985f-a973-442e-bbdf-885cfffeae5e/Untitled.png)

Tôi search "RCX:00000061h ^" thì thấy nó lặp lại 16 lần 

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7479f2b8-599f-42fc-9707-25d520b0c5a9/Untitled.png)

tương đương với size của file cho là 0x170 chia cho độ dài của key là 24 thì được kết quả như trong hình. Lúc này tôi khá chắc kèo là xor với key sẽ lặp lại mỗi 24 lần.

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/039fc662-6feb-4081-8085-4ab363307e30/Untitled.png)

Sau những chiêm nghiệm và phân tích trên, tôi viết thuật toán encrypt và encrypt 8 byte đầu của file PNG:

```python
table1=[90, 132, 6, 69, 174, 203, 232, 243, 87, 254, 166, 61, 94, 65, 8, 208, 51, 34, 
        33, 129, 32, 221, 0, 160, 35, 175, 113, 4, 139, 245, 24, 29, 225, 15, 101, 9, 
        206, 66, 120, 62, 195, 55, 202, 143, 100, 50, 224, 172, 222, 145, 124, 42, 192, 
        7, 244, 149, 159, 64, 83, 229, 103, 182, 122, 82, 78, 63, 131, 75, 201, 130, 114,
        46, 118, 28, 241, 30, 204, 183, 215, 199, 138, 16, 121, 26, 77, 25, 53, 22, 125, 
        67, 43, 205, 134, 171, 68, 146, 212, 14, 152, 20]

table2=[185, 155, 167, 36, 27, 60, 226, 58, 211, 240, 253, 79, 119, 
        209, 163, 12, 72, 128, 106, 218, 189, 216, 71, 91, 250, 150, 11, 236, 207, 73, 
        217, 17, 127, 177, 39, 231, 197, 178, 99, 230, 40, 54, 179, 93, 251, 220, 168, 
        112, 37, 246, 176, 156, 165, 95, 184, 57, 228, 133, 169, 252, 19, 2, 81, 48, 242, 
        105, 255, 116, 191, 89, 181, 70, 23, 194, 88, 97, 153, 235, 164, 158, 137, 238, 
        108, 239, 162, 144, 115, 140, 84, 188, 109, 219, 44, 214, 227, 161, 141, 80, 247, 52]

table3=[213, 249, 1, 123, 142, 190, 104, 107, 85, 157, 45, 237, 47, 
        147, 21, 31, 196, 136, 170, 248, 13, 92, 234, 86, 3, 193, 154, 56, 5, 111, 98, 74, 
        18, 223, 96, 148, 41, 117, 126, 173, 233, 10, 49, 180, 187, 186, 135, 59, 38, 210, 
        110, 102, 200, 76, 151, 198]

key = [97, 49, 49, 95, 109, 89, 95, 104, 111, 109, 49, 101, 115, 95, 104, 52, 116, 51, 95, 98, 52, 114, 100, 115]

def getValFromTable(byte):
    if(byte < 100):
        return table1[byte]
    elif(byte < 200 and byte >= 100):
        return table2[byte-100] 
    else:
        return table3[byte-200]

hexlist = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A	]
i=0
j=0
tmp2 = 0
tmp3 = 0
tmp4 = 0
tmp5 = 0
while True:
    if i >= len(hexlist):
        break
    byte = hexlist[j]
    if i & 1 == 0 :
        tmp2 = key[i%24] ^ getValFromTable(byte)
    else:
        tmpKey = key[i%24] ^ 0xFF
        tmp2 = tmpKey  ^ getValFromTable(byte)
    tmp3 = getValFromTable(tmp2)
    if ((tmp3 & 0x80) == 0x80):
        tmp4 = tmp3 ^ 0x42
        result = tmp4 ^ 0xff
        print(hex(result), end= " ")
    else:
        result = tmp3 ^ 0xff
        print(hex(result), end= " ")
    j += 1
    i += 1
```

Khi chạy thì thu được

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33348bf6-98a0-4b97-b737-86f965ddb7d2/Untitled.png)

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/691c8066-643b-40aa-8b02-5365202b24dc/Untitled.png)

Vậy là thuật toán ecrypt của tôi đúng. Thông qua thuật toán encrypt này, tôi sử dụng thuật toán kinh điển để decrypt, BRUTE FORCE:

```python
table1=[90, 132, 6, 69, 174, 203, 232, 243, 87, 254, 166, 61, 94, 65, 8, 208, 51, 34, 
        33, 129, 32, 221, 0, 160, 35, 175, 113, 4, 139, 245, 24, 29, 225, 15, 101, 9, 
        206, 66, 120, 62, 195, 55, 202, 143, 100, 50, 224, 172, 222, 145, 124, 42, 192, 
        7, 244, 149, 159, 64, 83, 229, 103, 182, 122, 82, 78, 63, 131, 75, 201, 130, 114,
        46, 118, 28, 241, 30, 204, 183, 215, 199, 138, 16, 121, 26, 77, 25, 53, 22, 125, 
        67, 43, 205, 134, 171, 68, 146, 212, 14, 152, 20]

table2=[185, 155, 167, 36, 27, 60, 226, 58, 211, 240, 253, 79, 119, 
        209, 163, 12, 72, 128, 106, 218, 189, 216, 71, 91, 250, 150, 11, 236, 207, 73, 
        217, 17, 127, 177, 39, 231, 197, 178, 99, 230, 40, 54, 179, 93, 251, 220, 168, 
        112, 37, 246, 176, 156, 165, 95, 184, 57, 228, 133, 169, 252, 19, 2, 81, 48, 242, 
        105, 255, 116, 191, 89, 181, 70, 23, 194, 88, 97, 153, 235, 164, 158, 137, 238, 
        108, 239, 162, 144, 115, 140, 84, 188, 109, 219, 44, 214, 227, 161, 141, 80, 247, 52]

table3=[213, 249, 1, 123, 142, 190, 104, 107, 85, 157, 45, 237, 47, 
        147, 21, 31, 196, 136, 170, 248, 13, 92, 234, 86, 3, 193, 154, 56, 5, 111, 98, 74, 
        18, 223, 96, 148, 41, 117, 126, 173, 233, 10, 49, 180, 187, 186, 135, 59, 38, 210, 
        110, 102, 200, 76, 151, 198]

key = [0x61, 0xCE, 0x31, 0xA0, 0x6D, 0xA6, 0x5F, 0x97, 0x6F, 0x92, 0x31, 0x9A, 0x73, 0xA0, 0x68, 0xCB, 0x74, 0xCC, 0x5F, 0x9D, 0x34, 0x8D, 0x64, 0x8C]
#key = [97, 49, 49, 95, 109, 89, 95, 104, 111, 109, 49, 101, 115, 95, 104, 52, 116, 51, 95, 98, 52, 114, 100, 115]

def getValFromTable(byte):
    if(byte < 100):
        return table1[byte]
    elif(byte < 200 and byte >= 100):
        return table2[byte-100] 
    else:
        return table3[byte-200]

def BruteToDie(byte, i):
    tmp2 = key[i%24] ^ getValFromTable(byte)
    tmp3 = getValFromTable(tmp2)
    if ((tmp3 & 0x80) == 0x80):
        tmp4 = tmp3 ^ 0x42
        result = tmp4 ^ 0xff
        return result
    else:
        result = tmp3 ^ 0xff
        return result
    

filein = open("cool_wizard_meme.png.encrypted","rb")
hexlist = list(filein.read())
filein.close()
j=0
fileout = open("_cool_wizard_meme.png","wb+")
for i in hexlist:
    tmp = 0
    while True:
        if BruteToDie(tmp, j) == i:
            tmp = tmp & 0xff
            fileout.write(tmp.to_bytes(1, 'little'))
            break
        else:
            tmp += 1
    j += 1
fileout.close()
print("DONE!")
```

Chạy file tôi thu được hình có flag:

![_cool_wizard_meme.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8e867010-e76e-4c89-86aa-641c196b7ecd/_cool_wizard_meme.png)

Done bài 10

![alt text](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6601121d-122b-45dc-ab0d-d82f463662a8/Untitled.png)
