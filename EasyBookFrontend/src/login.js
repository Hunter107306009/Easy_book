import "./login.css"
import axios from 'axios';
import Cookies from 'js-cookie';
import React, { useState, useEffect } from 'react';

function Login() {
	const [placeholder, setPlaceholder] = useState('初始占位符');

	let cus_login_Data=
  	{
	  	"phone": "",
	  	"pwd": ""
	}

	let res_login_Data=
	{
  		"RAccount": "",
  		"Rpwd": ""
	}

	function handleSelectChange(){
	    let selectedOption = document.getElementById("opt").value;
		if (selectedOption=="顧客")
		{
			setPlaceholder("手機號碼");
		}
		else if (selectedOption=="店家")
		{
			setPlaceholder("店家帳號");
		}
		else
		{
			console.log("選單判定出錯");
		}
	};

	function register_redirect(){
		window.location.href = "/signup";
	}

	function login_handle(){
		cus_login_Data.phone=document.getElementById("phone").value;
		cus_login_Data.pwd=document.getElementById("pwd").value;
		res_login_Data.RAccount=document.getElementById("phone").value;
		res_login_Data.Rpwd=document.getElementById("pwd").value;
		let opt=document.getElementById("opt").value;
		if (cus_login_Data.phone!="" && cus_login_Data.pwd!="" && opt=="顧客")
		{
			axios.post('http://127.0.0.1:8001/member/login', cus_login_Data)
			.then(response => {
				let responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					let currentTime = new Date();
					let expirationTime = new Date(currentTime.getTime() + (50 * 60 * 1000));
					Cookies.set('uesr_id', responseData.data, { expires: expirationTime });
					alert("登入成功");
					window.location.href = "/main";
				}
				else if (responseData.status=="error")
				{
					alert(responseData.msg);
				}
			})
			.catch(error => {
				console.log("!!!!!!!!!!");
				console.log(error);
			});
		}
		else if (res_login_Data.RAccount!="" && res_login_Data.Rpwd!="" && opt=="店家")
		{
			axios.post('http://127.0.0.1:8001/restaurant/restaurant_login', res_login_Data)
			.then(response => {
				let responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					let currentTime = new Date();
					let expirationTime = new Date(currentTime.getTime() + (50 * 60 * 1000));
					Cookies.set('restaurant_id', responseData.data.RID , { expires: expirationTime });
					alert("登入成功");
					window.location.href = "/book_manage";
				}
				else if (responseData.status=="error")
				{
					alert(responseData.msg);
				}
			})
			.catch(error => {
				console.log("!!!!!!!!!!");
				console.log(error);
			});
		}
		else
		{
			alert("尚有未填寫的欄位");
		}
	}
	
	useEffect(() => {
		handleSelectChange();
	}, []);

	return(
		<div>
			<div id ="original_body">
		        <div id ="login_body">
		            <div id="login_title">EasyBook</div>
		            
		            <div id="form_login">
		                <div id="form_select_user">
		                    <select className="form_select" id="opt" onChange={handleSelectChange}>
		                        <option value="顧客">顧客</option>
		                        <option value="店家">店家</option>
		                    </select>
		                </div>
		                <div className="login">
		                    <input type="text" id="phone" placeholder={placeholder} />
		                    <input type="password" id="pwd"  placeholder="密碼" />
		                    <div id="submit_wrap">
		                        <button id="login" className="btn" onClick={login_handle}>登入</button>
		                        <div id="register" onClick={register_redirect}>點我註冊</div>
		                    </div>
		                </div>
		            </div>
		        </div>
		    </div>
		</div>
	);
};

export default Login;