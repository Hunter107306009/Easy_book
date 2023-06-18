import "./main.css"
import "./banner.css"
import axios from 'axios';
import React, { useState , useEffect } from 'react';

function Main() {
	let  [res_message, set_res_message] = React.useState(null)

	function image_judge(url){
		if (url.length>15)
		{
			return url
		}
		else
		{
			return 'https://firebasestorage.googleapis.com/v0/b/test-4fa88.appspot.com/o/default.png?alt=media&token=2869477a-6cc5-48e4-a63e-0c329ee4e3c2'
		}
	}

	function personal_page() {
		window.location.href="/personal_page";
	};
	
	function book_page(event) {
		let clickedDiv = event.currentTarget;
	  	let divValue = clickedDiv.getAttribute('value');
		window.location.href="/book_page?RID="+divValue;
	};

	function book_page_search() {
		let query_name=document.getElementById("search").value;
		if (query_name!="")
		{
			axios.get('http://127.0.0.1:8001/restaurant/search_restaurant?restaurant_name='+query_name)
			.then(response => {
				let responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					if (responseData.data[0].RID!=null)
					{
						document.getElementById("search").value="";
						window.location.href="/book_page?RID="+responseData.data[0].RID;
					}
				}
				else if (responseData.status=="error")
				{
					document.getElementById("search").value="";
					alert(responseData.msg);
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
	};

	useEffect(() => {
		axios.get('http://127.0.0.1:8001/restaurant/restaurant_list')
		.then(response => {
			let responseData = response.data;
			console.log(responseData);
			if (responseData.status=="success")
			{
				set_res_message(responseData.data);
			}
			else if (responseData.status=="error")
			{
				//通常不會來到這行，這個api是單純要資料，不存在前端傳值有錯的可能
				alert(responseData.msg);
			}
		})
		.catch(error => {
			console.log(error);
		});
	}, []);

	function login_page(){
         window.location.href="/"
    }
	
	return(
		<div>
			<div id="banner">
				<div id="title">Easy Book</div>
				<div className="index" id="index2" onClick={personal_page}>會員資料</div>
				<div className="index" id="index1" style={{visibility:'hidden'}}>訂位紀錄</div>
				<div id="bolck"></div>
				<div id="index" style={{visibility:'hidden'}}>後臺管理</div>
                <button id="sign_up" onClick={login_page}>回登入頁</button>
			</div>
			<div id="page_body">
				<div id="search_box">
					<img id="search_bg" src={require('./icon/search_bg.jpg')}/>
					<div id="search_bg_block"></div>
					<div id="search_block">
						<div id="search_block_level2">
							<div id="search_description">查找想訂位的餐廳</div>
							<div id="search_icon_outside">
								<input id="search" placeholder="Search..."/>
								<img id="search_icon" src={require('./icon/search.png')} onClick={book_page_search}/>
							</div>
						</div>
					</div>
				</div>
				{
					res_message?.map((data, index) => {
						if (index % 4 === 0) {
						    return (
						   		<div id="restaurant_flex">
									<div id="restaurant_frame" value={data.RID} onClick={book_page}>
										<img id="restaurant_image_main" src={image_judge(data.URL)}/>
										<div id="restaurant_text_frame">
											<div id="restaurant_name_main">{data.RName}</div>
											<div id="restaurant_address">{data.RAddress}</div>
										</div>
									</div>
									{res_message[index + 1] && 
										<div id="restaurant_frame" value={res_message[index + 1].RID} onClick={book_page}>
											<img id="restaurant_image_main" src={image_judge(res_message[index + 1].URL)}/>
											<div id="restaurant_text_frame">
												<div id="restaurant_name_main">{res_message[index + 1].RName}</div>
												<div id="restaurant_address">{res_message[index + 1].RAddress}</div>
											</div>
										</div>
									}
									{res_message[index + 2] && 
										<div id="restaurant_frame" value={res_message[index + 2].RID} onClick={book_page}>
											<img id="restaurant_image_main" src={image_judge(res_message[index + 2].URL)}/>
											<div id="restaurant_text_frame">
												<div id="restaurant_name_main">{res_message[index + 2].RName}</div>
												<div id="restaurant_address">{res_message[index + 2].RAddress}</div>
											</div>
										</div>
									}
									{res_message[index + 3] && 
										<div id="restaurant_frame" value={res_message[index + 3].RID} onClick={book_page}>
											<img id="restaurant_image_main" src={image_judge(res_message[index + 3].URL)}/>
											<div id="restaurant_text_frame">
												<div id="restaurant_name_main">{res_message[index + 3].RAddress}</div>
												<div id="restaurant_address">{res_message[index + 3].RAddress}</div>
											</div>
										</div>
									}
								</div>
						    )
						}
					})
				}
			</div>
		</div>
	);
};

export default Main;