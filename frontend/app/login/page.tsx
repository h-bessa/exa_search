"use client";

import {Button} from '@nextui-org/react';
import {useEffect, useState} from "react";
import Login from "@/app/components/login/Login";

const Page = () => {

  const [apiState, setApiState] = useState({
    users: [],
    loading: false,
    error: '',
  });

  const {users, loading, error} = apiState


  useEffect(() => {
    const fetchUsers = async () => {
      setApiState((prevState) => ({...prevState, loading: true}))
      try {
        const result = await fetch('https://jsonplaceholder.typicode.com/users')
        if (!result.ok) {
          throw new Error('Network response was not ok');
        }
        const users = await result.json();
        setApiState({users: users, loading: false, error: ''});
      } catch (e: any) {
        setApiState({
          users: [],
          loading: false,
          error: `Error during data fetch - ${e.message}`,
        });
      }
    }
    fetchUsers();

  }, [])
  const handleLogin = () => {
    alert('Logged in!');
  };

  return (
    <Login />
  );
}

export default Page