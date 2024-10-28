import styles from './Footer.module.scss';
import stylesTema from 'styles/Tema.module.scss';
import classNames from 'classnames';
import { ReactComponent as Logo } from 'assets/logo.svg';

export default function Footer() {

  return (
    <footer className={styles.footer}>
      <Logo />
    </footer>
  );
}