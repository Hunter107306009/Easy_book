import "./banner.css"
import "./personal_page.css"
import axios from 'axios';
import React, { useState , useEffect } from 'react';

function PersonalPage() {
	let status=1;
	let middle_status=1;
	let [buttonColors, setButtonColors] = useState({
	  	btn1: "#272727",
		btn2: "#7B7B7B",
		btn3: "#7B7B7B",
		btn4: "#7B7B7B"
	});

	let [rightMainBlocks, setRightMainBlocks] = useState({
	  	rightMainBlock1: "flex",
	  	rightMainBlock2: "none",
	  	rightMainBlock3: "none",
	  	rightMainBlock4: "none"
	});

	let [MbuttonColors, setMButtonColors] = useState({
	  	Mbtn1: "#272727",
	  	Mbtn2: "#7B7B7B"
	});

	let [MrightMainBlocks, setMRightMainBlocks] = useState({
	  	MrightMainBlock1: "flex",
	  	MrightMainBlock2: "none"
	});

	let [draws, setDraws] = React.useState([])
	let [user_name, set_user_name] = React.useState([])
	
	let [consumption_data, set_consumption_data] = React.useState([])
	let [consumption_list, set_consumption_list] = React.useState([])

	let new_cus_Data=
  	{
	  	"ID": "",
 		"name": "",
 		"pwd": ""
	}

	function home_page() {
		window.location.href="/main";
	};

	function cus_modify(event) {
		let clickedDiv = event.currentTarget;
		let cus_ReNumber = clickedDiv.getAttribute('value-ReNumber');
		let cus_Rid = clickedDiv.getAttribute('value-Rid');
		window.location.href="/cus_modify/?data1="+cus_ReNumber+"&data2="+cus_Rid;
	};

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

	function setCookie(name, value, days) {
	  	var expires = "";
	  	if (days) {
	    	var date = new Date();
	    	date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
	    	expires = "; expires=" + date.toUTCString();
	  	}
	  	document.cookie = name + "=" + value + expires + "; path=/";
	}

	function deleteCookie(name) {
	  document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
	}

	function modifyJSON(json){
		return JSON.parse(decodeURIComponent(json));
	}

	function get_user_name()
	{
		if (modifyJSON(getCookie("uesr_id"))!=null)
		{
			axios.get('http://127.0.0.1:8001/member/get_member_info?id='+modifyJSON(getCookie("uesr_id")).ID).then(function (response) {
				console.log(response)
				if (response.data!=null)
				{
					set_user_name(response.data.data.Name)
				}
				else
				{
					console.log("無法取得使用者名稱");
				}
			})
			.catch(error => {
				console.log(error);
			});
		}
		else if(modifyJSON(getCookie("uesr_id"))==null)
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
	}

	function cus_book_record_handle(){
		if (modifyJSON(getCookie("uesr_id"))!=null)
		{
			axios.get('http://127.0.0.1:8001/book/query_book_member?MemberID='+modifyJSON(getCookie("uesr_id")).ID).then(function (response) {
				console.log(response)
				if (response.data!=null)
				{
					setDraws(response.data.data)
				}
				else
				{
					console.log("取得訂位紀錄的資料有誤");
				}
			})
			.catch(error => {
				console.log(error);
			});
		}
		else if(modifyJSON(getCookie("uesr_id"))==null)
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
	}

	useEffect(() => {
		if (getCookie("uesr_id")==null)
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
	    judje_color_and_display();
	    judje_middle_color_and_display();
	    cus_book_record_handle();
	    get_consumption_data();
	    get_user_name();
	}, []);

	function renew_cus(){
		console.log(modifyJSON(getCookie("uesr_id")));
		new_cus_Data.name=document.getElementById("new_name").value;
		new_cus_Data.pwd=document.getElementById("new_pwd").value;
		if (getCookie("uesr_id")!=null)
		{
			new_cus_Data.ID=modifyJSON(getCookie("uesr_id")).ID;
		}
		if (new_cus_Data.ID!=null && new_cus_Data.name!="" && new_cus_Data.pwd!="")
		{
			axios.patch('http://127.0.0.1:8001/member/update_member', new_cus_Data)
			.then(response => {
				let responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					alert("修改成功");
					window.location.reload();
				}
				else if (responseData.status=="error")
				{
					alert(responseData.msg);
				}
			})
			.catch(error => {
				console.log(error);
			});
		}
		else if(new_cus_Data.ID==null)
		{
			alert("Cookie已過期，請重新登入");
			window.location.href = "/";
		}
		else
		{
			alert("尚有未填寫的欄位");
		}
	}

	function get_consumption_data(){
		if (getCookie("uesr_id")!=null)
		{
			axios.get('http://127.0.0.1:8001/member/get_member_paypoints_info?id='+modifyJSON(getCookie("uesr_id")).ID)
			.then(response => {
				let responseData = response.data;
				console.log(responseData);
				if (responseData.status=="success")
				{
					set_consumption_data(responseData.data);
					set_consumption_list(responseData.data.Points_list);
					console.log(responseData.data);
					console.log(responseData.data.Points_list);
				}
				else if (responseData.status=="error")
				{
					console.log(responseData);
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

	function judje_color_and_display() {
		if (status==1)
		{
			setButtonColors({
		      	btn1: "#272727",
			  	btn2: "#7B7B7B",
			  	btn3: "#7B7B7B",
			  	btn4: "#7B7B7B"
		    });

		    setRightMainBlocks({
		      	rightMainBlock1: "flex",
			  	rightMainBlock2: "none",
			  	rightMainBlock3: "none",
			  	rightMainBlock4: "none"
		    });
		}
		else if (status==2)
		{
			setButtonColors({
		      	btn1: "#7B7B7B",
			  	btn2: "#272727",
			  	btn3: "#7B7B7B",
			  	btn4: "#7B7B7B"
		    });

		    setRightMainBlocks({
		      	rightMainBlock1: "none",
			  	rightMainBlock2: "flex",
			  	rightMainBlock3: "none",
			  	rightMainBlock4: "none"
		    });
		}
		else if (status==3)
		{
			setButtonColors({
		      	btn1: "#7B7B7B",
			  	btn2: "#7B7B7B",
			  	btn3: "#272727",
			  	btn4: "#7B7B7B"
		    });

		    setRightMainBlocks({
		      	rightMainBlock1: "none",
			  	rightMainBlock2: "none",
			  	rightMainBlock3: "flex",
			  	rightMainBlock4: "none"
		    });
		}
		else if (status==4)
		{
			setButtonColors({
		      	btn1: "#7B7B7B",
			  	btn2: "#7B7B7B",
			  	btn3: "#7B7B7B",
			  	btn4: "#272727"
		    });

		    setRightMainBlocks({
		      	rightMainBlock1: "none",
			  	rightMainBlock2: "none",
			  	rightMainBlock3: "none",
			  	rightMainBlock4: "flex"
		    });
		}
		else
		{
			alert("前端的索引值出錯");
		}
	}

	function judje_middle_color_and_display() {
		if (middle_status==1)
		{
			setMButtonColors({
		      	Mbtn1: "#272727",
			  	Mbtn2: "#7B7B7B"
		    });

		    setMRightMainBlocks({
		      	MrightMainBlock1: "flex",
			  	MrightMainBlock2: "none"
		    });
		}
		else if (middle_status==2)
		{
			setMButtonColors({
		      	Mbtn1: "#7B7B7B",
			  	Mbtn2: "#272727"
		    });

		    setMRightMainBlocks({
		      	MrightMainBlock1: "none",
			  	MrightMainBlock2: "flex"
		    });
		}
		else
		{
			alert("middle前端的索引值出錯");
		}
	}

	function btn1() {
		status=1;
	  	judje_color_and_display();
	};

	function btn2(){
		status=2;
	  	judje_color_and_display();
	};

	function btn3(){
		status=3;
	  	judje_color_and_display();
	};

	function btn4(){
		status=4;
	  	judje_color_and_display();
	};

	function middle_title1(){
		middle_status=1;
  		judje_middle_color_and_display();
	}

	function middle_title2(){
		middle_status=2;
  		judje_middle_color_and_display();
	}

    function delete_handle(event){
        let clickedDiv = event.currentTarget;
        let divValue = clickedDiv.getAttribute('value');
        axios.delete('http://127.0.0.1:8001/book/cancel_book?ReNumber='+divValue)
        .then(response => {
            let responseData = response.data;
            if (responseData.status=="success")
            {
                document.getElementById("book_record"+clickedDiv.getAttribute('value-id')).style.display = 'none';
                alert("已取消訂位");
            }
            else if (responseData.detail=="不能取消訂位")
            {
                alert("訂位不符合取消條件");
            }
            else
            {
                alert("取消遭拒");
            }
        })
        .catch(error => {
            console.log(error);
            alert("訂位不符合取消資格");
        });
    }

    function login_page(){
         window.location.href="/"
    }

	return(
		<div>
			<div id="banner">
				<div id="title">Easy Book</div>
				<div className="index" id="index1" onClick={home_page}>首頁</div>
				<div className="index" id="index1" style={{visibility:'hidden'}}>訂位紀錄</div>
				<div id="bolck"></div>
				<div id="index" style={{visibility:'hidden'}}>後臺管理</div>
                <button id="sign_up" onClick={login_page}>回登入頁</button>
			</div>
			<div id="personal_body_wrap">
				<div id="personal_body">
					<div id="personal_tite">
						<div id="personal_name">{user_name}</div>
						<img id="personal_img" src={require('./icon/crown.png')}/>
						<div id="personal_LV">LV{consumption_data.MLevel}</div>
					</div>
					<div id="personal_main">
						<div id="left_main_wrap">
							<div id="left_tag_wrap">
								<div id="btn1" onClick={btn1} style={{color: buttonColors.btn1}} className="left_tag">訂位紀錄</div>
								<div id="btn2" onClick={btn2} style={{color: buttonColors.btn2}} className="left_tag">消費紀錄</div>
								<div id="btn3" onClick={btn3} style={{color: buttonColors.btn3}} className="left_tag">會員點數</div>
								<div id="btn4" onClick={btn4} style={{color: buttonColors.btn4}} className="left_tag">修改會員資料</div>
							</div>
						</div>
						<div id="right_main_wrap">
							<div className="right_main_block" id="right_main_block1" style={{display:rightMainBlocks.rightMainBlock1}}>
								<div id="right_main_block_title_wrap">
									<div id="right_main_block_title">近期訂位</div>	
								</div>
								<div id="book_record_frame">
								{console.log(draws)}
								{
									draws?.map((data, index) => {
										return (
											<div className="book_record" id={`book_record${index}`}>
												<img className="record_image" src={image_judge(data.RURL)}/>
												<div className="book_record_right">
													<div className="book_record_right_line1">{data.RName}</div>
													<div className="book_record_right_line2"><img className="book_record_right_line2_image" src={require('./icon/correct.png')}/><div className="book_record_right_line2_text">已確認訂位</div></div>
													<div className="book_record_right_line3"><img className="book_record_right_line3_image" src={require('./icon/user.png')}/><div className="book_record_right_line3_text">{data.RePerson}</div><img className="book_record_right_line3_image2" src={require('./icon/calendar.png')}/><div className="book_record_right_line3_text">{data.ReTime}</div></div>
												</div>
												<div id="event_box" value-ReNumber={data.ReNumber} value-ReNumber={data.ReNumber} value-Rid={data.RID} onClick={cus_modify}></div>
												<div id="cross_frame">
													<img id="cross" src={require('./icon/cross.png')} value={data.ReNumber} value-id={index} onClick={delete_handle}/>
												</div>
											</div>
										)
									})
								}
								</div>
							</div>
							<div className="right_main_block" id="right_main_block2" style={{display:rightMainBlocks.rightMainBlock2}}>
								<div id="right_main_block_title_wrap">
									<div id="right_main_block_title">累積消費金額</div>
									<div id="right_main_block_NT">NT.{consumption_data.MAccumSpend}</div>
								</div>
								<div id="info">
									{
										consumption_list?.map((data, index) => {
											return (
												<div id="info_body">
													<div id="info_body_left">
														<div className="info_body_left_name1">{data.RestaurantName}</div>
														<div className="info_body_left_name2" style={{visibility:'hidden'}}>京站店</div>
														<div className="info_body_left_name2">{data.CTime}</div>
													</div>
													<div id="info_body_right">
														<div className="info_body_right_name">NT.{data.Consumptions}</div>
													</div>
												</div>
											)
										})
									}
									
								</div>
							</div>
							<div className="right_main_block" id="right_main_block3" style={{display:rightMainBlocks.rightMainBlock3}}>
								<div id="right_main_block_title_wrap">
									<div id="right_main_block_title">累積點數</div>
									<div id="right_main_block_point">{consumption_data.MPoints}點</div>
								</div>
								<div id="point_middle_wrap" style={{display:'none'}}></div>
								<div id="info">
									{
										consumption_list?.map((data, index) => {
											return (
												<div id="info_body">
													<div id="info_body_left">
														<div className="info_body_left_name1">{data.RestaurantName}</div>
														<div className="info_body_left_name2" style={{visibility:'hidden'}}>京站店</div>
														<div className="info_body_left_name2">{data.CTime}</div>
													</div>
													<div id="info_body_right">
														<div className="info_body_right_name">+{data.PointsChange}點</div>
													</div>
												</div>
											)
										})
									}
								</div>
							</div>
							<div className="right_main_block" id="right_main_block4" style={{display:rightMainBlocks.rightMainBlock4}}>
								<div id="right_main_block_title_wrap">
									<div id="right_main_block_title">設定會員基本資料</div>
								</div>
								<div id="user_setting_frame">
									<input type="text" id="new_name" className="user_setting_input" placeholder="請輸入姓名"/>
									<input type="password" id="new_pwd" className="user_setting_input" placeholder="請輸入您的新密碼"/>
									<button id="user_setting_btn" onClick={renew_cus}>提交</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	  );
};

export default PersonalPage;