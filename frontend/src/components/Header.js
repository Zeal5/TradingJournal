import styles from "../styles/components/header.module.css";
import { useRouter } from "next/router";

export default function Header() {
  const router = useRouter();
  const goto_dashboard = () => {
    router.push('/dashboard')
  } 

  return (
    <div className={styles.mainheader}>
      <div className={styles.header}>
        Header
        <span className={styles.dashboard}>
          <button onClick={goto_dashboard}>DashBoard</button>
        </span>
      </div>
    </div>
  );
}
