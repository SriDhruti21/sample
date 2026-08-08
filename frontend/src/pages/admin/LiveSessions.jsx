import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { useSession } from "../../context/SessionContext";
import AdminLayout from "./AdminLayout";

const API = "http://127.0.0.1:5000";

function LiveSessions() {
  const { user } = useSession();
  const [sessions, setSessions] = useState([]);

  useEffect(() => {
    const load = () => {
      axios
        .get(`${API}/api/admin/sessions/live?user_id=${user.user_id}`)
        .then((res) => {
          if (res.data.success) setSessions(res.data.sessions);
        });
    };
    load();
    const interval = setInterval(load, 10000); // refresh every 10s
    return () => clearInterval(interval);
  }, [user]);

  return (
    <AdminLayout title="Live Sessions">
      <div className="admin-card">
        <table className="admin-table">
          <thead>
            <tr>
              <th>Session ID</th>
              <th>User</th>
              <th>Cart Value</th>
              <th>Risk</th>
              <th>Last Activity</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {sessions.map((s) => (
              <tr key={s.session_id}>
                <td>{s.session_id?.slice(0, 10)}...</td>
                <td>{s.user_id?.slice(0, 8) || "Guest"}</td>
                <td>${s.cart_value?.toFixed(2) || "0.00"}</td>
                <td>
                  <span className={`risk-${s.risk_level || "LOW"}`}>
                    {s.risk_level || "—"}
                  </span>
                </td>
                <td>{new Date(s.last_activity).toLocaleTimeString()}</td>
                <td>
                  <Link
                    to={`/admin/session/${s.session_id}`}
                    className="view-btn"
                  >
                    Open
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {sessions.length === 0 && (
          <p className="empty-text">No live sessions right now</p>
        )}
      </div>
    </AdminLayout>
  );
}

export default LiveSessions;