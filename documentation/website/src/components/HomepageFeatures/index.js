import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";

const FeatureList = [
  {
    title: "Quick start",
    Svg: require("@site/static/img/1_quickstart.svg").default,
    description: (
      <>Get started quickly to play with the Zenon Ecosystem and APIs.</>
    ),
  },
  {
    title: "Wallet",
    Svg: require("@site/static/img/2_wallet.svg").default,
    description: (
      <>
        Comes with Wallet utilities so you can start building on top of it right
        away.
      </>
    ),
  },
  {
    title: "Examples",
    Svg: require("@site/static/img/3_examples.svg").default,
    description: (
      <>
        Examples for JSON-RPC client, Wallet, Embedded APIs and other usecases.
      </>
    ),
  },
];

function Feature({ Svg, title, description }) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
