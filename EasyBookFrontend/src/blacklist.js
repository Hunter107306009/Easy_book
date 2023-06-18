import "./blacklist.css"
import axios from 'axios';
import Cookies from 'js-cookie';
import React, { useState, useEffect } from 'react';

function Blacklist() {
	const [black_list, set_black_list] = useState(null);

	let black_user={ 
		"Phone": "",
   		"NonArrive": null 
	}

	function new_black_user(){
		black_user.Phone=document.getElementById("phone").value;
		black_user.NonArrive=1;
		if (black_user.Phone!="" && black_user.NonArrive!=null)
		{
			axios.post('http://127.0.0.1:8001/restaurant/add_to_blacklist',black_user).then(function (response) {
				console.log(response)
				if (response.data!=null)
				{
					alert("新增黑名單成功");
					window.location.reload();
				}
				else
				{
					console.log("新增黑名單的功能有誤");
				}
			})
			.catch(error => {
				console.log(error);
			});			
		}
		else
		{
			alert("尚有欄位未填寫完畢");
		}
	}

	function get_black_user(){
		axios.get('http://127.0.0.1:8001/restaurant/blacklist_list').then(function (response) {
			console.log(response)
			if (response.data!=null)
			{
				set_black_list(response.data.data)
			}
			else
			{
				console.log("取得黑名單的功能有誤");
			}
		})
		.catch(error => {
			console.log(error);
		});			
	}

	useEffect(() => {
		get_black_user();
	}, []);

	return(
		<div>
			<div id="blacklist_wrap">
				<div id="blacklist_center">
					<div id="blacklist_top">
						<div id="blacklist_title">新增黑名單用戶</div>
						<div id="blacklist_form">
							<input type="text" id="phone" className="input_decorate" placeholder="黑名單電話"/>
							<button className="input_button_decorate" onClick={new_black_user}>加入</button>
						</div>
					</div>
					<div id="blacklist_bottom">
						<div id="blacklist_title">查詢黑名單用戶</div>
					</div>
					<div id="blacklist_bottom_ans">
					{
						black_list?.map((data, index) => {
							return (
								<div className="black_L_unit">
									<div className="black_L_text">{data.Name}</div>
									<div className="black_L_text">/</div>
									<div className="black_L_text">{data.Phone}</div>
									<div className="black_L_text">/</div>
									<div className="black_L_text">{data.NonArrive}次未到</div>			
								</div>
							)
						})
					}
					</div>
				</div>
			</div>
		</div>
	);
};

export default Blacklist;