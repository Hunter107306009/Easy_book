import "./cus_modify.css"
import axios from 'axios';
import Cookies from 'js-cookie';
import React, { useState, useEffect } from 'react';

function Cus_modify() {
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

	const urlParams = new URLSearchParams(window.location.search);
	const renumber = urlParams.get('data1');
	const rid = urlParams.get('data2');
	

	let change_data={
	    "ReNumber": null,
	    "ID": null,
	    "RID": null,
	    "BookTime": "",
	    "Person": null,
	    "Reason": "",
	}

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

	function personal_page(){
		window.location.href = "/personal_page";
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

	function modifyJSON(json){
		return JSON.parse(decodeURIComponent(json));
	}

	function change(){
		if (getCookie("uesr_id")!=null){
			change_data.ReNumber=renumber;
			change_data.ID=modifyJSON(getCookie("uesr_id")).ID;
			change_data.RID=rid;
			change_data.BookTime=formatDateToISO(now.getFullYear()+" "+document.getElementById("Day").value+" "+document.getElementById("Time").value);
			change_data.Person=document.getElementById("Person").value[0]
			change_data.Reason=document.getElementById("reason").value
			if (change_data.ReNumber!=null && change_data.ID!=null && change_data.RID!=null && change_data.BookTime!="" && change_data.Person!=null && change_data.Reason!="")
			{
				console.log(change_data);
				axios.patch('http://127.0.0.1:8001/book/update_book', change_data)
				.then(response => {
					let responseData = response.data;
					console.log(responseData);
					if (responseData.status=="success")
					{
						alert("修改成功");
						personal_page();
					}
					else if (responseData.status=="error")
					{
						alert(responseData.msg);
					}
					else
					{
						alert("修改遭拒");
					}
				})
				.catch(error => {
					console.log(error);
				});
			}
			else
			{
				alert("尚有未填寫的欄位");
			}
		}
		else
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
		
	}

	

	useEffect(() => {

	}, []);

	return(
		<div>
			<div id="checkout_wrap">
				<div id="checkout_center">
					<div className="form-container">
						<select className="select_container" id="Day">
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
					<div className="form-container">
						<select className="select_container" id="Time">
							<option>11:00</option>
							<option>12:00</option>
							<option>13:00</option>
							<option>17:00</option>
							<option>18:00</option>
							<option>19:00</option>
							<option>20:00</option>
						</select>
					</div>
					<div className="form-container">
						<select className="select_container" id="Person">
							<option>1位</option>
							<option>2位</option>
							<option>3位</option>
							<option>4位</option>
							<option>5位</option>
							<option>6位</option>
						</select>
					</div>
					<input className="input-container" id="reason" type="text" placeholder="修改原因"/>
					<button className="btn" onClick={change}>更新訂位</button>
					<div id="go_back" onClick={personal_page}>回個人資料頁面</div>
				</div>
			</div>
		
		</div>
	);
};

export default Cus_modify;