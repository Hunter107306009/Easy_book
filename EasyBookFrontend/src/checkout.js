import "./checkout.css"
import axios from 'axios';
import Cookies from 'js-cookie';
import React, { useState, useEffect } from 'react';

function Checkout() {
	const [res_name, set_res_name] = useState("???");

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

	function get_restaurant_name(){
		if (getCookie("restaurant_id")!=null)
		{
			axios.get('http://127.0.0.1:8001/restaurant/restaurant_info?restaurant_id='+getCookie("restaurant_id")).then(function (response) {
				console.log(response)
				if (response.data!=null)
				{
					set_res_name(response.data.data[0].RName)
					console.log("取得餐廳名稱成功");
				}
				else
				{
					console.log("取得餐廳名稱的功能有誤");
				}
			})
			.catch(error => {
				console.log(error);
			});			
		}
		else
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
	}

	
	let checkout_Data=
  	{
	    "Phone": "",
	    "RID": null,
	    "Consumptions": ""
	}


	function consumption_handle(){
		checkout_Data.Phone=document.getElementById("consumption_phone").value;
		checkout_Data.RID=parseInt(getCookie("restaurant_id"));
		checkout_Data.Consumptions=document.getElementById("consumption_sum").value;
		console.log(checkout_Data);
		if (checkout_Data.Phone!="" && checkout_Data.Consumptions!="" && checkout_Data.RID!=null)
		{
			console.log(checkout_Data.Consumptions);
			axios.post('http://127.0.0.1:8001/restaurant/add_consumption_record', checkout_Data)
			.then(response => {
				let responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					alert("結帳成功");
				}
				else if (responseData.status=="error")
				{
					alert(responseData.msg);
				}
				else
				{
					alert("結帳遭拒，請確認填寫的資訊是否有誤");
				}
			})
			.catch(error => {
				console.log(error);
			});
		}
		else if (checkout_Data.RID==null)
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
		else
		{
			alert("尚有欄位未填寫完畢");
		}
	}

	

	useEffect(() => {
		get_restaurant_name();
	}, []);

	return(
		<div>
			<div id="checkout_wrap">
				<div id="checkout_center">
					<input className="input-container" id="restaurant_name" type="text" placeholder={res_name} readOnly/>
					<input className="input-container" id="consumption_phone" type="text" placeholder="顧客電話"/>
					<input className="input-container" id="consumption_sum" type="text" placeholder="消費金額"/>
					<button className="btn" onClick={consumption_handle}>結帳</button>
				</div>
			</div>
		</div>
	);
};

export default Checkout;