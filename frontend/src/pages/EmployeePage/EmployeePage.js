import React from "react";
import { useEffect, useState } from "react";
import useAuth from "../../hooks/useAuth";

import axios from "axios";

const EmployeePage = () => {

  const [user, token] = useAuth();
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        let response = await axios.get("http://127.0.0.1:8000/api/employees/", {
          headers: {
            Authorization: "Bearer " + token,
          },
        });
        setEmployees(response.data);
      } catch (error) {
        console.log(error.response.data);
      }
    };
    fetchEmployees();
  }, [token]);
  return (
    <div className="container">
      <h1>Employee Page</h1>
      {employees &&
        employees.map((employee) => (
          <div key={employee.id}>
            {employee.id}
            <br />
            {employee.name}
            <div>
              {employee.picture.thumbnail} <img src={employee.thumbnail} alt={employee.picture} width={"200px"} height={"200px"}/>

            </div>
          </div>
        ))}
    </div>
  );
};

export default EmployeePage;
