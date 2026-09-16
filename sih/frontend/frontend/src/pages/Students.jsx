import { useEffect, useState } from "react";
import { getStudents } from "../services/governmentService";

const Students = () => {

  const [students, setStudents] = useState([]);

  useEffect(() => {
    loadStudents();
  }, []);

  const loadStudents = async () => {
    try {

      const response = await getStudents();

      console.log("Students API Response:", response);

      setStudents(response.data || []);

    } catch (error) {

      console.error("Failed to load students:", error);

    }
  };

  return (
    <div className="p-6">

      <h1 className="text-3xl font-bold mb-6">
        Students
      </h1>

      <div className="bg-white rounded-xl shadow overflow-hidden">

        <table className="w-full">

          <thead className="bg-green-100">

            <tr>
              <th className="p-3 text-left">ID</th>
              <th className="p-3 text-left">Name</th>
              <th className="p-3 text-left">College</th>
              <th className="p-3 text-left">Location</th>
            </tr>

          </thead>

          <tbody>

            {students.length > 0 ? (

              students.map((student) => (

                <tr
                  key={student.student_id}
                  className="border-b hover:bg-green-50"
                >

                  <td className="p-3">
                    {student.student_id}
                  </td>

                  <td className="p-3">
                    {student.student_name}
                  </td>

                  <td className="p-3">
                    {student.college_name}
                  </td>

                  <td className="p-3">
                    {student.location}
                  </td>

                </tr>

              ))

            ) : (

              <tr>

                <td
                  colSpan="4"
                  className="p-6 text-center text-gray-500"
                >
                  No students found
                </td>

              </tr>

            )}

          </tbody>

        </table>

      </div>

    </div>
  );
};

export default Students;