import "./login.css"
import axios from 'axios';
import React, { useState, useEffect } from 'react';

function Signup() {
	let [Showdiv, setShowdiv] = useState({
	  	div1: "block",
	  	div2: "none"
	});

  	let cus_register_Data=
  	{
    	"name": "",
  		"phone": "",
  		"pwd": ""
  	}

  	let res_register_Data=
  	{
  		"RAccount": "",
  		"Rpwd": "",
  		"RName": "",
  		"RPhone": "",
  		"RAddress": "",
  		"Url": ""
  	}

  	function login_redirect(){
		window.location.href = "/";
	}

	function handleSelectChange(){
	    let selectedOption = document.getElementById("opt").value;
		if (selectedOption=="顧客")
		{
			setShowdiv({
		      	div1: "block",
	  			div2: "none"
		    });
		}
		else if (selectedOption=="店家")
		{
			setShowdiv({
		      	div1: "none",
	  			div2: "block"
		    });
		}
		else
		{
			console.log("選單判定出錯");
		}
	}

	function signup_handle(){
		cus_register_Data.name=document.getElementById("name").value;
		cus_register_Data.phone=document.getElementById("phone").value;
		cus_register_Data.pwd=document.getElementById("pwd").value;
		res_register_Data.RAccount=document.getElementById("RAccount").value;
		res_register_Data.Rpwd=document.getElementById("Rpwd").value;
		res_register_Data.RName=document.getElementById("RName").value;
		res_register_Data.RPhone=document.getElementById("RPhone").value;
		res_register_Data.RAddress=document.getElementById("RAddress").value;
		res_register_Data.Url=document.getElementById("Url").value;
		let opt=document.getElementById("opt").value;
		if (cus_register_Data.name!="" && cus_register_Data.phone!="" && cus_register_Data.pwd!="" && opt=="顧客")
		{
			axios.post('http://127.0.0.1:8001/member/create_member', cus_register_Data)
			.then(response => {
				const responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					alert("註冊成功");
					login_redirect();
				}
				else if (responseData.status=="error")
				{
					//執行這行，通常是電話已經被註冊過
					alert(responseData.msg);
				}
			})
				.catch(error => {
				console.log(error);
				console.log("!!!!!!!!!!");
			});
		}
		else if(res_register_Data.RAccount!="" && res_register_Data.Rpwd!="" && res_register_Data.RName!="" && res_register_Data.RPhone!="" && res_register_Data.RAddress!="" && res_register_Data.Url!="" && opt=="店家")
		{
			axios.post('http://127.0.0.1:8001/restaurant/create_restaurant', res_register_Data)
			.then(response => {
				const responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					alert("註冊成功");
					login_redirect();
				}
				else if (responseData.status=="error")
				{
					//執行這行，通常是帳號已經被註冊過
					alert(responseData.msg);
				}
			})
				.catch(error => {
				console.log(error);
				console.log("!!!!!!!!!!");
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
		                <div className="login" id="cus_div" style={{display:Showdiv.div1}}>
		                	<input className="input"  type="text" id="name" placeholder="姓名"/>
		                    <input className="input"  type="text" id="phone" placeholder="手機號碼" />
		                    <input className="input"  type="password" id="pwd"  placeholder="密碼" />
		                    <div id="submit_wrap">
		                        <button id="login" className="btn" onClick={signup_handle}>註冊</button>
		                        <div id="register" onClick={login_redirect}>回到登入</div>
		                    </div>
		                </div>
		                <div className="login" id="res_div" style={{display:Showdiv.div2}}>
		                	<input className="input" type="text" id="RAccount" placeholder="帳號"/>
		                    <input className="input" type="password" id="Rpwd" placeholder="密碼" />
		                    <input className="input" type="text" id="RName"  placeholder="店家名稱" />
		                    <input className="input" type="text" id="RPhone"  placeholder="店家電話" />
		                    <input className="input" type="text" id="RAddress"  placeholder="店家地址" />
		                    <input className="input" type="text" id="Url"  placeholder="店家照片URL" />
		                    <div id="submit_wrap">
		                        <button id="login" className="btn" onClick={signup_handle}>註冊</button>
		                        <div id="register" onClick={login_redirect}>回到登入</div>
		                    </div>
		                </div>
		            </div>
		        </div>
		    </div>
		</div>
	);
};

export default Signup;