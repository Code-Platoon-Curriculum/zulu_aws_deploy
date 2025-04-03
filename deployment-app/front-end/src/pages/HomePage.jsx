import { useOutletContext } from "react-router-dom";
import { useState, useEffect } from "react";
import { getLists } from "../utilities";

const HomePage = () => {
    const { user, lists, setLists } = useOutletContext()

    useEffect(() => {
        const handleGetLists = async () => {
            const responseData = await getLists();
            console.log('response data', responseData);
            setLists(responseData);
        }
        handleGetLists();
    }, []);

    console.log(lists);
    return(
        <>
            <h1>HomePage</h1>
            <h2>Display name: {user ? user.display_name : ""}</h2>
            <h2>Email: {user ? user.email : ""}</h2>
        </>

    )
}

export default HomePage;