import "./checkout.css"
import axios from 'axios';
import Cookies from 'js-cookie';
import React, { useState, useEffect } from 'react';

function ReRegister() {
	let new_res_data=
	{
    	"RPwd": "",
    	"RID": null,
    	"RName": "",
    	"RPhone": "",
    	"RAddress": "",
    	"URL": ""
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

	function new_res_data_handle(){
		if (getCookie("restaurant_id")!=null)
		{
			new_res_data.RPwd=document.getElementById("new_pwd").value;
			new_res_data.RID=getCookie("restaurant_id");
			new_res_data.RName=document.getElementById("new_name").value;
			new_res_data.RPhone=document.getElementById("new_phone").value;
			new_res_data.RAddress=document.getElementById("new_address").value;
			new_res_data.URL=document.getElementById("new_url").value;
			if (new_res_data.RPwd!="" && new_res_data.RID!=null && new_res_data.RName!="" && new_res_data.RPhone!="" && new_res_data.RAddress!="" && new_res_data.URL!="")
			{
				axios.patch('http://127.0.0.1:8001/restaurant/update_restaurant_info',new_res_data).then(function (response) {
					console.log(response)
					if (response.data!=null)
					{
						alert("更新餐廳資料成功");
					}
					else
					{
						console.log("更新餐廳資料的功能有誤");
					}
				})
				.catch(error => {
					console.log(error);
				});	
			}
			else
			{
				alert("尚有資訊未填寫完畢");
			}	
		}
		else
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
	}

	return(
		<div>
			<div id="checkout_wrap">
				<div id="checkout_center">
					<input className="input-container" id="new_pwd" type="text" placeholder="餐廳新密碼"/>
					<input className="input-container" id="new_name" type="text" placeholder="餐廳新名稱"/>
					<input className="input-container" id="new_phone" type="text" placeholder="餐廳新電話"/>
					<input className="input-container" id="new_address" type="text" placeholder="餐廳新地址"/>
					<input className="input-container" id="new_url" type="text" placeholder="餐廳新圖片"/>
					<button className="btn" onClick={new_res_data_handle}>更新餐廳資訊</button>
				</div>
			</div>
		</div>
	);
};

export default ReRegister;