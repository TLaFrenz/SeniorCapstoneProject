import React, { useEffect, useState } from 'react'
import UserAdapter from '../adapters/UserAdapter';
import CustomerDisplay from '../components/CustomerDisplay';
import CustomerNavbar from '../components/CustomerNavbar';
import Services from '../components/Services';
import CustomerJobDisplay from '../components/CustomerJobDisplay'; 
import { homeObjOne } from '../components/CustomerDisplay/Data';
import Footer from '../components/Footer';
import ServicesAdapter from '../adapters/ServicesAdapter';


const CustomerPortal = () => {
  const [ user, setUser ] = useState({});
  const [ currentJob, setCurrentJob ] = useState();

  useEffect(() => {
    UserAdapter.getLoggedInUser()
    .then(resp => resp.json())
    .then(resp => {  
      console.log(resp)
      setUser(resp)
      ServicesAdapter.getCurrentJob()
      .then(resp => resp.json())
      .then(setCurrentJob)
      .catch(console.log) 
    })
    .catch(console.log)
  }, [])



  console.log(currentJob)
  return (
    <div>
        <CustomerNavbar />
        <CustomerDisplay />
        { currentJob ? <CustomerJobDisplay job={currentJob} />: <Services /> }
        <CustomerDisplay {...homeObjOne}/>
        <h1> { 'Hello ! ' + user.fname+ ' ' + user.lname } </h1>
        <h2> { user.username } </h2>
        <h3> { user.address } </h3>
        <h4> { user.DOB } </h4>
        <h5> { user.email } </h5>
        <h6> { user.phone_number } </h6>

        <Footer />

    </div>
  )
}

export default CustomerPortal