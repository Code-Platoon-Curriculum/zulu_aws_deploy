import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import NavBar from './components/NavBar'
import { Outlet, useLoaderData } from 'react-router-dom'
import { api } from './utilities'

const testConnection = async() => {
  console.log('testconnection')
  const response = await api.get("lists/test/");
  console.log(response)
}

function App() {
  const loadedUser = useLoaderData();
  const [user, setUser] = useState(loadedUser);
  const [ lists, setLists ] = useState([]);

  useEffect(() => {
    testConnection();
  }, [])

  useEffect(() => {
    console.log('<App/> state user ', user)
  }, [user])


  return (
    <>
      <NavBar user={user} setUser={setUser} />
      <Outlet context={{ user, setUser, lists, setLists }}/>
    </>
  )
}

export default App
