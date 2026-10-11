// GET /api/vault-stats
// Reads the live counts the Vault publishes on vault.jrstrengthandfitness.com/pricing
// ("88 Resources · 34 Systems & frameworks · 26 Interactive tools · 11 Workflows"), so the numbers on
// jrstrengthandfitness.com follow the Vault as resources are added. Cached at the edge for an hour.
// If the Vault can't be reached or its wording changes, it returns 502 and the page keeps its built-in numbers.

const SOURCE = "https://vault.jrstrengthandfitness.com/pricing";
const LABELS = {
  resources: /(\d[\d,]*)\s*Resources\b/i,
  systems: /(\d[\d,]*)\s*Systems\s*(?:&amp;|&)\s*frameworks\b/i,
  tools: /(\d[\d,]*)\s*Interactive tools\b/i,
  workflows: /(\d[\d,]*)\s*Workflows\b/i,
};

function parse(html) {
  const text = html
    .replace(/<script[\s\S]*?<\/script>/gi, " ")
    .replace(/<style[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ");
  const out = {};
  for (const [key, re] of Object.entries(LABELS)) {
    const m = text.match(re);
    if (!m) return null;
    out[key] = parseInt(m[1].replace(/,/g, ""), 10);
  }
  return out;
}

async function handler(req, res) {
  try {
    const r = await fetch(SOURCE, { headers: { "user-agent": "jrstrengthandfitness.com vault-stats" } });
    if (!r.ok) throw new Error("vault responded " + r.status);
    const stats = parse(await r.text());
    if (!stats) throw new Error("counts not found on the Vault pricing page");
    res.setHeader("Cache-Control", "public, s-maxage=3600, stale-while-revalidate=86400");
    res.status(200).json({ ...stats, source: SOURCE });
  } catch (e) {
    res.setHeader("Cache-Control", "public, s-maxage=300");
    res.status(502).json({ error: String(e.message || e) });
  }
}

module.exports = handler;
module.exports.parse = parse;
