// Run: node scripts/create_builder_pack_link.js
// Requires: STRIPE_SECRET_KEY in env
import Stripe from "stripe";

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
  apiVersion: "2025-07-30.basil",
});

const SITE = process.env.SITE_URL || "https://ikwe.ai";

async function main() {
  const link = await stripe.paymentLinks.create({
    line_items: [
      {
        quantity: 1,
        price_data: {
          currency: "usd",
          unit_amount: 250000, // $2,500.00
          product_data: {
            name: "Ikwe AI Risk System — Builder’s Blueprint",
            description:
              "Core assessment frameworks, templates, and anonymized audit examples. Copy, adapt, and run. No implementation support.",
          },
        },
      },
    ],
    after_completion: {
      type: "redirect",
      redirect: {
        url: `${SITE}/thanks-preview?session_id={CHECKOUT_SESSION_ID}`,
      },
    },
  });

  console.log("\n✅ Builder’s Blueprint Payment Link created:\n");
  console.log(link.url);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
