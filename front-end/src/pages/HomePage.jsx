import { useOutletContext } from "react-router-dom";
import { useState, useEffect } from "react";
import { getLists } from "../utilities";
import ListDisplay from "../components/ListDisplay";

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
            { lists.length ? <ListDisplay lists={lists}/> : null}
        </>

    )
}

export default HomePage;