import "./banner.css"
import "./book_manage.css"
import axios from 'axios';
import React, { useState , useEffect } from 'react';

function Book_manage() {
    let [res_book, set_res_book] = React.useState([])

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

    function checkout() {
        window.open("./checkout", "_blank", "width=800,height=600");
    };

    function blacklist() {
        window.open("./blacklist", "_blank", "width=800,height=600");
    };

    function res_reRegister() {
        window.open("./res_reRegister", "_blank", "width=800,height=600");
    }

    function res_book_record_handle(){
        if (getCookie("restaurant_id")!=null)
        {
            axios.get('http://127.0.0.1:8001/book/query_book_restaurant?RID='+getCookie("restaurant_id")).then(function (response) {
                console.log(response)
                if (response.data!=null)
                {
                    set_res_book(response.data.data)
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
        else if(getCookie("restaurant_id")==null)
        {
            alert("Cookie已過期，請重新登入");
            window.location.href = "/";
        }
    }

    function delete_handle(event){
        let clickedDiv = event.currentTarget;
        let divValue = clickedDiv.getAttribute('value');
        console.log({"ReNumber":parseInt(divValue)});
        axios.delete('http://127.0.0.1:8001/book/cancel_book?ReNumber='+divValue)
        .then(response => {
            let responseData = response.data;
            if (responseData.status=="success")
            {
                document.getElementById("book_record_frame"+clickedDiv.getAttribute('value-id')).style.display = 'none';
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

    function modifyDate(date){
        return date.match(/\d{4}-\d{2}-\d{2} \d{2}:\d{2}/)[0];
    }

    function res_modify(event) {
        let clickedDiv = event.currentTarget;
        let cus_ReNumber = clickedDiv.getAttribute('value-ReNumber');
        let cus_id = clickedDiv.getAttribute('value-id');
        window.location.href="/res_modify/?data1="+cus_ReNumber+"&data2="+cus_id;
    };

    useEffect(() => {
        res_book_record_handle();
    }, []);

    function login_page(){
         window.location.href="/"
    } 

    return(
        <div>
            <div id="banner">
                <div id="title">Easy Book</div>
                <div className="index" id="index2" onClick={checkout}>顧客結帳</div>
                <div className="index" id="index3" onClick={blacklist}>黑名單管理</div>
                <div className="index" id="index3" onClick={res_reRegister}>更新餐廳資訊</div>
                <div id="index" style={{visibility:'hidden'}}>後臺管理</div>
                <div id="bolck"></div>
                <button id="sign_up" onClick={login_page}>回登入頁</button>
            </div>
            <div id="body_wrap">
                <div id="right_body">
                    <div id="right_body_head_block" style={{visibility:'hidden'}}>遮擋區塊 應當隱藏</div>

                    {
                        res_book?.map((data, index) => {
                            return (
                                <div className="book_record_frame" id={`book_record_frame${index}`}>
                                    <img id="book_record_image" src={require('./icon/profile-user.png')}/>
                                    <div className="book_record_part1">
                                        <div className="book_record_part1_name">{data.MName}</div>
                                        <div className="book_record_part1_phone">{data.MPhone}</div>
                                    </div>
                                    <div className="book_record_part2">{data.RePerson}</div>
                                    <div className="book_record_part3">{data.ReTNo}</div>
                                    <div className="book_record_part4">
                                        <div className="book_record_part4_time">{modifyDate(data.ReTime)}</div>
                                    </div>
                                    <div id="event_box" value-ReNumber={data.ReNumber} value-id={data.MemberID} onClick={res_modify}></div>
                                    <div id="cross_frame">
                                        <img id="cross" value={data.ReNumber} value-id={index} onClick={delete_handle} src={require('./icon/cross.png')}/>
                                    </div>
                                </div>        
                            )
                        })
                    }
                    
                </div>
            </div>
        </div>
    );
};

export default Book_manage;