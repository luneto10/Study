import cardapio from 'data/cardapio.json';
import styles from './Inicio.module.scss';
import Menu from 'components/Menu';

export default function Inicio() {
  let pratosRecomendados = [...cardapio];
  pratosRecomendados = pratosRecomendados.sort(() => 0.5 - Math.random()).splice(0,3);
  return (
    <section>
      <h3 className={styles.titulo}>
                Recomendacoes da cozinha
      </h3>

      <div className={styles.recomendados}>
        {pratosRecomendados.map(item => (
          <div key={item.id} className={styles.recomendado}>
            <div className={styles.recomendado__imagem}>
              <img src={item.photo} alt={item.title} />
            </div>
            <button className={styles.recomendado__botao}>
                Ver Mais
            </button>
          </div>))
        }
      </div>

    </section>
  );
}