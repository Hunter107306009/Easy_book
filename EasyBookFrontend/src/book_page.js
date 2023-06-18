import "./banner.css"
import "./book_page.css"
import axios from 'axios';
import Cookies from 'js-cookie';
import React, { useState, useEffect } from 'react';

function Book_page() {
	const now = new Date();
	const d0 = new Date(now);
	const [TodayDate, setTodayDate] = useState((d0.getMonth() + 1)+"月"+(d0.getDate())+"日");
	const d1 = new Date(now);
	d1.setDate(d0.getDate() + 1);
	const [TodayDate1, setTodayDate1] = useState((d1.getMonth() + 1)+"月"+(d1.getDate())+"日");
	const d2 = new Date(now);
	d2.setDate(d0.getDate() + 2);
	const [TodayDate2, setTodayDate2] = useState((d2.getMonth() + 1)+"月"+(d2.getDate())+"日");
	const d3 = new Date(now);
	d3.setDate(d0.getDate() + 3);
	const [TodayDate3, setTodayDate3] = useState((d3.getMonth() + 1)+"月"+(d3.getDate())+"日");
	const d4 = new Date(now);
	d4.setDate(d0.getDate() + 4);
	const [TodayDate4, setTodayDate4] = useState((d4.getMonth() + 1)+"月"+(d4.getDate())+"日");
	const d5 = new Date(now);
	d5.setDate(d0.getDate() + 5);
	const [TodayDate5, setTodayDate5] = useState((d5.getMonth() + 1)+"月"+(d5.getDate())+"日");
	const d6 = new Date(now);
	d6.setDate(d0.getDate() + 6);
	const [TodayDate6, setTodayDate6] = useState((d6.getMonth() + 1)+"月"+(d6.getDate())+"日");
	const d7 = new Date(now);
	d7.setDate(d0.getDate() + 7);
	const [TodayDate7, setTodayDate7] = useState((d7.getMonth() + 1)+"月"+(d7.getDate())+"日");
	const d8 = new Date(now);
	d8.setDate(d0.getDate() + 8);
	const [TodayDate8, setTodayDate8] = useState((d8.getMonth() + 1)+"月"+(d8.getDate())+"日");
	const d9 = new Date(now);
	d9.setDate(d0.getDate() + 9);
	const [TodayDate9, setTodayDate9] = useState((d9.getMonth() + 1)+"月"+(d9.getDate())+"日");
	const d10 = new Date(now);
	d10.setDate(d0.getDate() + 10);
	const [TodayDate10, setTodayDate10] = useState((d10.getMonth() + 1)+"月"+(d10.getDate())+"日");

	const [SelectedDate, setSelectedDate] = useState((d0.getMonth() + 1)+"月"+(d0.getDate())+"日");
	const [SelectedTime, setSelectedTime] = useState(null);

	const urlParams = new URLSearchParams(window.location.search);
	const rid = urlParams.get('RID');
	const [msg_name, set_msg_name] = useState(null);
	const [msg_address, set_msg_address] = useState(null);
	const [msg_phone, set_msg_phone] = useState(null);
	let [small_box_status,set_small_box_status] = useState([
	  	"auto",
	  	"auto",
	  	"auto",
	  	"auto",
	  	"auto",
	  	"auto",
	  	"auto"
	]);
	let [small_box_color,set_small_box_color]=useState([
	  	"#FF6347",
	  	"#FF6347",
	  	"#FF6347",
	  	"#FF6347",
	  	"#FF6347",
	  	"#FF6347",
	  	"#FF6347"
	]);

	let book_Data=
  	{
		"ID": null,
		"RID": null,
		"Name": "",
		"Phone": "",
		"Reason": "",
		"ReTime": "",
		"Person": null	
	}

	let seats_needed=
	{
		"RID": null,
		"BookTime":"",
		"Person":null
	}

	function get_restaurant_msg()
	{
		axios.get('http://127.0.0.1:8001/restaurant/restaurant_info?restaurant_id='+rid).then(function (response) {
			let responseData = response.data;
			console.log(responseData)
			if (responseData.status=="success")
			{
				set_msg_name(responseData.data[0].RName)
				set_msg_address(responseData.data[0].RAddress)
				set_msg_phone(responseData.data[0].RPhone)
				console.log("取得餐廳資訊成功");
			}
			else if (responseData.status=="error")
			{
				alert(responseData.msg);
				home_page();
			}
			else
			{
				alert("查無此餐廳資訊");
				home_page();
			}
		})
		.catch(error => {
			console.log(error);
		});
	}


	function home_page() {
		window.location.href="/main";
	};
	function personal_page() {
		window.location.href="/personal_page";
	};

	function getCookie(name) {
	  	const cookieString = document.cookie;
	  	const cookies = cookieString.split(';');

	  	for (let i = 0; i < cookies.length; i++) {
	    	const cookie = cookies[i].trim();
	    	if (cookie.startsWith(name + '=')) {
	      		return cookie.substring(name.length + 1);
	    	}
	  	}
	  	return null;
	}

	function modifyJSON(json){
		return JSON.parse(decodeURIComponent(json));
	}

	async function set_sub_page_box_date(){
		await setSelectedDate(document.getElementById("selected_date").value);
		await handle_sub_page_right_box();
	}

	function getClicckTime(event) {
	  	let clickedDiv = event.currentTarget;
	  	let divValue = clickedDiv.getAttribute('value');
	  	setSelectedTime(divValue+":00");
	}

	function formatDateToISO(inputDate) {
	  	let convertedDate = inputDate.replace('月', '-').replace('日', '');

		let date = new Date(convertedDate);
		let year = date.getFullYear();
		let month = (date.getMonth() + 1).toString().padStart(2, '0');
		let day = date.getDate().toString().padStart(2, '0');

		let hours = date.getHours().toString().padStart(2, '0');
		let minutes = date.getMinutes().toString().padStart(2, '0');

		let formattedDate = `${year}-${month}-${day} ${hours}:${minutes}:00`;
		return formattedDate
	}

	function book_handle(){
		if (getCookie("uesr_id")!=null)
        {
        	if (modifyJSON(getCookie("uesr_id"))!=null)
			{
				book_Data.ID=modifyJSON(getCookie("uesr_id")).ID;
				book_Data.Name=modifyJSON(getCookie("uesr_id")).Name;
				book_Data.Phone=modifyJSON(getCookie("uesr_id")).Phone;
			}
			book_Data.RID=rid;
			book_Data.Reason=document.getElementById("Reason").value;
			if (SelectedDate!=null && SelectedTime!=null)
			{
				book_Data.ReTime=formatDateToISO(now.getFullYear()+" "+SelectedDate+" "+SelectedTime);
			}
			book_Data.Person=parseInt(document.getElementById("Person").value[0]);
			console.log(book_Data);
			if (book_Data.ID!=null && book_Data.RID!=null && book_Data.Person!=null && book_Data.Name!="" && book_Data.Phone!="" && book_Data.Reason!="" && book_Data.ReTime!="")
			{
				axios.post('http://127.0.0.1:8001/book/book', book_Data)
				.then(response => {
					let responseData = response.data;
					console.log(responseData);
					if (responseData.status=="success")
					{
						alert("訂位成功");
					}
					else if (responseData.status=="error")
					{
						alert(responseData.msg);
					}
					else
					{
						alert("訂位遭拒");
					}
				})
				.catch(error => {
					console.log(error);
				});			
			}
			else if(book_Data.ID==null)
			{
				alert("Cookie已過期，請重新登入");
				window.location.href = "/";
			}
			else if(book_Data.RID==null)
			{
				alert("本餐廳已不提供訂位服務");
				home_page();
			}
			else
			{
				alert("尚有欄位未填寫完畢");
			}
        }
        else if(getCookie("uesr_id")==null)
        {
            alert("Cookie已過期，請重新登入");
            window.location.href = "/";
        }
	}

	function handle_sub_page_right_box()
	{
		seats_needed.RID=rid;
		seats_needed.Person=document.getElementById("Person").value[0];
		seats_needed.BookTime=(now.getFullYear()+" "+"0"+ document.getElementById("selected_date").value).replace(" ","-").replace("月","-").replace("日","");

		if (seats_needed.RID!=null && seats_needed.Person!=null && seats_needed.BookTime!=""){
			console.log(seats_needed);
			axios.post('http://127.0.0.1:8001/book/check_seats', seats_needed)
			.then(response => {
				let responseData = response.data;
				if (responseData.status=="success")
				{
					if (responseData.data.length==7)
					{
						let small_box_status_Temporary=[]
						let small_box_color_Temporary=[]
						for (let i = 0; i < 7; i++) {
							if (responseData.data[i].available==true)
							{
								small_box_status_Temporary.push("auto");
								small_box_color_Temporary.push("#FF6347");
							}
							else
							{
								small_box_status_Temporary.push("none");
								small_box_color_Temporary.push("#ADADAD");
							}
						}
						console.log(responseData.data);
						console.log(small_box_color_Temporary);
						set_small_box_status(small_box_status_Temporary);
      					set_small_box_color(small_box_color_Temporary);	
					}
					console.log("獲取當前選項位置資訊");
				}
				else
				{
					console.log("獲取到錯誤的選項位置資訊");
				}
			})
			.catch(error => {
				console.log(error);
				console.log("獲取當前選項位置有意外狀況");
			});
		}
		else if(seats_needed.RID==null)
		{
			alert("Rid不應該為空，請重新從首頁進入本頁面");
			home_page();
		}
		else
		{
			console.log("發生意料之外的錯誤");
		}
	}

	useEffect(() => {
		set_sub_page_box_date();
		get_restaurant_msg();
	}, []);

	function login_page(){
         window.location.href="/"
    }

	return(
		<div>
			<div id="banner">
				<div id="title">Easy Book</div>
				<div className="index" id="index1" onClick={home_page}>首頁</div>
				<div className="index" id="index1" onClick={personal_page}>會員資料</div>
				<div id="bolck"></div>
				<div id="index" style={{visibility:'hidden'}}>後臺管理</div>
                <button id="sign_up" onClick={login_page}>回登入頁</button>
			</div>
			<div id="book_body">
				<div id="title1">{msg_name}</div>
				<div id="title1_sub">{msg_address}</div>
				<div id="title1_sub">{msg_phone}</div>
				<div id="seg_decoration">
					<img id="seg_decoration_icon" src={require('./icon/calendar_orange.png')}/>
					<div id="seg_decoration_text">我要訂位</div>
				</div>
				<div id="title2">選擇訂位時段</div>
				<div id="form_wrap">
					<div id="form_number_of_people">
						<div id="form_title">用餐人數</div>
						<div id="form_select_wrap">
							<select className="form_select" id="Person" onChange={handle_sub_page_right_box}>
							    <option>1位</option>
							    <option>2位</option>
							    <option>3位</option>
							    <option>4位</option>
							    <option>5位</option>
							    <option>6位</option>
							</select>
						</div>
					</div>
					<div id="form_reason">
						<div id="form_title">用餐原因</div>
						<div id="form_select_wrap">
							<select className="form_select" id="Reason">
							    <option>家庭聚餐</option>
							    <option>朋友聚會</option>
							    <option>商務宴請</option>
							    <option>情侶聚會</option>
							    <option>生日聚會</option>
							    <option>其他</option>
							</select>
						</div>
					</div>
					<div id="form_date">
						<div id="form_title">用餐日期</div>
						<select className="form_select_date" id="selected_date" onChange={set_sub_page_box_date}>
							<option>{TodayDate}</option>
							<option>{TodayDate1}</option>
							<option>{TodayDate2}</option>
							<option>{TodayDate3}</option>
							<option>{TodayDate4}</option>
							<option>{TodayDate5}</option>
							<option>{TodayDate6}</option>
							<option>{TodayDate7}</option>
							<option>{TodayDate8}</option>
							<option>{TodayDate9}</option>
							<option>{TodayDate10}</option>
						</select>
					</div>
				</div>
				<div id="restaurnt_sub_page">
					<img id="restaurant_image" src={require('./icon/restaurant1.jpg')}/>
					<div id="restaurnt_sub_page_right">
						<div id="restaurnt_sub_page_right_title">{msg_name}</div>
						<div id="restaurnt_sub_page_right_address">{msg_address}</div>
						<div id="restaurnt_sub_page_right_annotation" style={{visibility:'hidden'}}>目前尚餘可訂位時段</div>
						<div id="restaurnt_sub_page_right_box_wrap">
							<div value="11" className="restaurnt_sub_page_right_box" tabIndex="0" onClick={getClicckTime} style={{pointerEvents:small_box_status[0],backgroundColor:small_box_color[0]}}>
								<div id="11_date" className="restaurnt_sub_page_right_box1">{SelectedDate}</div>
								<div id="11_time" className="restaurnt_sub_page_right_box2">11:00</div>
							</div>
							<div value="12" className="restaurnt_sub_page_right_box" tabIndex="0" onClick={getClicckTime} style={{pointerEvents:small_box_status[1],backgroundColor:small_box_color[1]}}>
								<div id="12_date" className="restaurnt_sub_page_right_box1">{SelectedDate}</div>
								<div id="12_time" className="restaurnt_sub_page_right_box2">12:00</div>
							</div>
							<div value="13" className="restaurnt_sub_page_right_box" tabIndex="0" onClick={getClicckTime} style={{pointerEvents:small_box_status[2],backgroundColor:small_box_color[2]}}>
								<div id="13_date" className="restaurnt_sub_page_right_box1">{SelectedDate}</div>
								<div id="13_time" className="restaurnt_sub_page_right_box2">13:00</div>
							</div>
							<div value="17" className="restaurnt_sub_page_right_box" tabIndex="0" onClick={getClicckTime} style={{pointerEvents:small_box_status[3],backgroundColor:small_box_color[3]}}>
								<div id="17_date" className="restaurnt_sub_page_right_box1">{SelectedDate}</div>
								<div id="17_time" className="restaurnt_sub_page_right_box2">17:00</div>
							</div>
							<div value="18" className="restaurnt_sub_page_right_box" tabIndex="0" onClick={getClicckTime} style={{pointerEvents:small_box_status[4],backgroundColor:small_box_color[4]}}>
								<div id="18_date" className="restaurnt_sub_page_right_box1">{SelectedDate}</div>
								<div id="18_time" className="restaurnt_sub_page_right_box2">18:00</div>
							</div>
							<div value="19" className="restaurnt_sub_page_right_box" tabIndex="0" onClick={getClicckTime} style={{pointerEvents:small_box_status[5],backgroundColor:small_box_color[5]}}>
								<div id="19_date" className="restaurnt_sub_page_right_box1">{SelectedDate}</div>
								<div id="19_time" className="restaurnt_sub_page_right_box2">19:00</div>
							</div>
							<div value="20" className="restaurnt_sub_page_right_box" tabIndex="0" onClick={getClicckTime} style={{pointerEvents:small_box_status[6],backgroundColor:small_box_color[6]}}>
								<div id="20_date" className="restaurnt_sub_page_right_box1">{SelectedDate}</div>
								<div id="20_time" className="restaurnt_sub_page_right_box2">20:00</div>
							</div>
						</div>
					</div>
					<button id="book_btn" onClick={book_handle}>送出訂位</button>
				</div>
			</div>
		</div>
	);
};

export default Book_page;