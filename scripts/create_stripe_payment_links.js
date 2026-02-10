// Run: node scripts/create_stripe_payment_links.js
// Requires env: STRIPE_SECRET_KEY and SITE_URL
// This creates Payment Links with inline price_data (products + prices created automatically).

import Stripe from "stripe";

const secretKey = process.env.STRIPE_SECRET_KEY;
if (!secretKey) {
  console.error("Missing STRIPE_SECRET_KEY in env.");
  process.exit(1);
}

const SITE = process.env.SITE_URL || "https://ikwe.ai";

const stripe = new Stripe(secretKey, {
  apiVersion: "2025-07-30.basil",
});

async function createPaymentLink({ name, description, amountUsd, successPath }) {
  const link = await stripe.paymentLinks.create({
    line_items: [
      {
        quantity: 1,
        price_data: {
          currency: "usd",
          unit_amount: Math.round(amountUsd * 100),
          product_data: { name, description },
        },
      },
    ],
    after_completion: {
      type: "redirect",
      redirect: { url: `${SITE}${successPath}?session_id={CHECKOUT_SESSION_ID}` },
    },
    allow_promotion_codes: true,
  });

  return link.url;
}

async function main() {
  const previewUrl = await createPaymentLink({
    name: "Ikwe AI Risk System — System Blueprint",
    description:
      "Redacted sample output from a completed Ikwe AI Risk Audit (not customized). Includes sample scorecard, before/after example, and methodology overview.",
    amountUsd: 2500,
    successPath: "/thanks-preview",
  });

  const playbookUrl = await createPaymentLink({
    name: "Ikwe AI Risk Audit — Playbook",
    description:
      "Self-implementation playbook for AI risk scoring, governance, failure-class mapping, and templates. Not an audit of your company.",
    amountUsd: 5000,
    successPath: "/thanks-playbook",
  });

  console.log("\n✅ Stripe Payment Links created:\n");
  console.log("System Blueprint:", previewUrl);
  console.log("Playbook:", playbookUrl);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
