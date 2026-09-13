import { useState, useMemo } from "react";

const MS_SYSTEMS = [
  // ICP-MS family
  { id: "Q-ICP-MS", name: "Quadrupole ICP-MS", family: "ICP-MS",
    intro: "Solution nebulization", ion: "Inductively Coupled Plasma", optics: "Extraction cones + ion lenses + collision/reaction cell",
    analyzer: "Quadrupole", detector: "Electron multiplier (dual mode)",
    use: "Trace element concentrations", freq: "Very High" },
  { id: "QQQ-ICP-MS", name: "Triple Quadrupole ICP-MS/MS", family: "ICP-MS",
    intro: "Solution nebulization", ion: "Inductively Coupled Plasma", optics: "Extraction cones + ion lenses",
    analyzer: "Triple quadrupole (Q1-CRC-Q2)", detector: "Electron multiplier (dual mode)",
    use: "Trace elements with enhanced interference removal", freq: "High" },
  { id: "HR-ICP-MS", name: "High-Resolution ICP-MS", family: "ICP-MS",
    intro: "Solution nebulization", ion: "Inductively Coupled Plasma", optics: "Extraction cones + ion lenses + ESA",
    analyzer: "Double-focusing magnetic sector", detector: "Electron multiplier / Faraday",
    use: "Trace elements at high mass resolution", freq: "Medium" },
  { id: "MC-ICP-MS", name: "Multi-Collector ICP-MS", family: "ICP-MS",
    intro: "Solution nebulization", ion: "Inductively Coupled Plasma", optics: "Extraction cones + ion lenses + ESA",
    analyzer: "Double-focusing magnetic sector", detector: "Faraday cup array + ion counters",
    use: "High-precision isotope ratios", freq: "High" },
  { id: "LA-Q-ICP-MS", name: "LA-ICP-MS (Quadrupole)", family: "ICP-MS",
    intro: "Laser ablation", ion: "Inductively Coupled Plasma", optics: "Extraction cones + ion lenses + collision/reaction cell",
    analyzer: "Quadrupole", detector: "Electron multiplier (dual mode)",
    use: "In situ trace element mapping/spot analysis", freq: "High" },
  { id: "LA-MC-ICP-MS", name: "LA-MC-ICP-MS", family: "ICP-MS",
    intro: "Laser ablation", ion: "Inductively Coupled Plasma", optics: "Extraction cones + ion lenses + ESA",
    analyzer: "Double-focusing magnetic sector", detector: "Faraday cup array + ion counters",
    use: "In situ isotope ratios (U-Pb, Hf, etc.)", freq: "High" },
  { id: "LA-ICP-TOF", name: "LA-ICP-TOF-MS", family: "ICP-MS",
    intro: "Laser ablation", ion: "Inductively Coupled Plasma", optics: "Extraction cones + ion lenses",
    analyzer: "Time-of-flight", detector: "Microchannel plate / electron multiplier",
    use: "Fast multi-element imaging, all masses simultaneous", freq: "Low-Medium" },

  // TIMS
  { id: "TIMS", name: "TIMS (single collector)", family: "TIMS",
    intro: "Filament loading (Re/Ta)", ion: "Thermal ionization (surface)", optics: "Electrostatic extraction + ion lenses",
    analyzer: "Magnetic sector (single-focusing)", detector: "Faraday cup / electron multiplier",
    use: "Isotope ratios, geochronology", freq: "Medium" },
  { id: "MC-TIMS", name: "Multi-Collector TIMS", family: "TIMS",
    intro: "Filament loading (Re/Ta)", ion: "Thermal ionization (surface)", optics: "Electrostatic extraction + ion lenses + ESA",
    analyzer: "Double-focusing magnetic sector", detector: "Faraday cup array + ion counters",
    use: "High-precision isotope ratios (Sr, Nd, Pb, Os, U)", freq: "High" },
  { id: "N-TIMS", name: "Negative TIMS", family: "TIMS",
    intro: "Filament loading", ion: "Thermal ionization (negative ions)", optics: "Electrostatic extraction + ion lenses + ESA",
    analyzer: "Double-focusing magnetic sector", detector: "Faraday cup array + ion counters",
    use: "Os, B isotopes (negative ion mode)", freq: "Low" },

  // SIMS
  { id: "SIMS", name: "Large-geometry SIMS", family: "SIMS",
    intro: "Primary ion beam sputtering (O⁻/Cs⁺)", ion: "Ion sputtering (secondary ions)", optics: "Electrostatic extraction + ESA + transfer optics",
    analyzer: "Double-focusing magnetic sector", detector: "Faraday cup + electron multiplier",
    use: "In situ isotope ratios, trace elements, U-Pb dating", freq: "Medium" },
  { id: "SHRIMP", name: "SHRIMP", family: "SIMS",
    intro: "Primary ion beam sputtering (O₂⁻)", ion: "Ion sputtering (secondary ions)", optics: "Electrostatic extraction + ESA + transfer optics",
    analyzer: "Double-focusing magnetic sector (large radius)", detector: "Faraday cup + electron multiplier",
    use: "U-Pb zircon geochronology, high mass resolution", freq: "Medium" },
  { id: "NanoSIMS", name: "NanoSIMS", family: "SIMS",
    intro: "Primary ion beam sputtering (Cs⁺/O⁻, coaxial)", ion: "Ion sputtering (secondary ions)", optics: "Coaxial extraction + ESA + transfer optics",
    analyzer: "Double-focusing magnetic sector", detector: "Electron multiplier array (5–7 detectors)",
    use: "Sub-100nm isotopic imaging, presolar grains", freq: "Medium" },
  { id: "ToF-SIMS", name: "ToF-SIMS", family: "SIMS",
    intro: "Primary ion beam sputtering (Bi₃⁺/Ga⁺/C₆₀⁺)", ion: "Ion sputtering (secondary ions)", optics: "Pulsed extraction + reflectron",
    analyzer: "Time-of-flight (reflectron)", detector: "Microchannel plate",
    use: "Surface molecular imaging, depth profiling", freq: "Low-Medium" },

  // IRMS
  { id: "GS-IRMS", name: "Gas Source IRMS (continuous flow)", family: "IRMS",
    intro: "Elemental analyzer / gas bench", ion: "Electron ionization (Nier source)", optics: "Ion lenses + acceleration",
    analyzer: "Magnetic sector (single-focusing)", detector: "Faraday cup array (3–6 cups)",
    use: "Bulk stable isotopes (C, N, O, S, H)", freq: "Very High" },
  { id: "GC-IRMS", name: "GC-C-IRMS", family: "IRMS",
    intro: "GC separation + combustion/pyrolysis interface", ion: "Electron ionization (Nier source)", optics: "Ion lenses + acceleration",
    analyzer: "Magnetic sector (single-focusing)", detector: "Faraday cup array (3–6 cups)",
    use: "Compound-specific stable isotopes", freq: "High" },
  { id: "DI-IRMS", name: "Dual Inlet IRMS", family: "IRMS",
    intro: "Dual inlet (sample vs reference gas)", ion: "Electron ionization (Nier source)", optics: "Ion lenses + acceleration",
    analyzer: "Magnetic sector (single-focusing)", detector: "Faraday cup array",
    use: "High-precision bulk isotope ratios", freq: "Medium" },
  { id: "CRDS", name: "Cavity Ring-Down Spectroscopy (laser)", family: "IRMS",
    intro: "Gas introduction to optical cavity", ion: "None (optical absorption)", optics: "N/A (optical cavity mirrors)",
    analyzer: "N/A (laser wavelength scanning)", detector: "Photodetector",
    use: "Water isotopes (δ¹⁸O, δD), CO₂ isotopes", freq: "High" },

  // Noble gas
  { id: "NGMS", name: "Noble Gas Static MS", family: "Noble Gas",
    intro: "Vacuum extraction line (furnace/laser) + cryogenic separation", ion: "Electron ionization (Baur-Signer/Nier source)", optics: "Electrostatic extraction + ion lenses",
    analyzer: "Magnetic sector", detector: "Faraday cup + electron multiplier / Daly",
    use: "He, Ne, Ar, Kr, Xe isotopes, thermochronology", freq: "Medium" },
  { id: "ArAr-MS", name: "⁴⁰Ar/³⁹Ar MS", family: "Noble Gas",
    intro: "Laser/furnace extraction + getter purification", ion: "Electron ionization", optics: "Electrostatic extraction + ion lenses",
    analyzer: "Magnetic sector (multicollector)", detector: "Faraday cup + electron multiplier",
    use: "⁴⁰Ar/³⁹Ar geochronology", freq: "High" },
  { id: "RI-TOF-NGMS", name: "Resonance Ionization TOF Noble Gas MS", family: "Noble Gas",
    intro: "Laser/furnace extraction + getter purification", ion: "Resonance ionization (tunable lasers)", optics: "Pulsed extraction",
    analyzer: "Time-of-flight", detector: "Microchannel plate / electron multiplier",
    use: "Isobar-free noble gas isotope analysis", freq: "Very Low" },

  // GC-MS family
  { id: "GC-MS", name: "GC-MS (Quadrupole)", family: "GC-MS",
    intro: "GC separation (liquid injection or headspace)", ion: "Electron ionization (EI)", optics: "Ion lenses",
    analyzer: "Quadrupole", detector: "Electron multiplier",
    use: "Organic compound identification", freq: "Very High" },
  { id: "GC-MSMS", name: "GC-MS/MS (Triple Quad)", family: "GC-MS",
    intro: "GC separation", ion: "Electron ionization (EI)", optics: "Ion lenses",
    analyzer: "Triple quadrupole", detector: "Electron multiplier",
    use: "Targeted organics, MRM quantification", freq: "High" },
  { id: "Py-GC-MS", name: "Py-GC-MS", family: "GC-MS",
    intro: "Pyrolysis + GC separation", ion: "Electron ionization (EI)", optics: "Ion lenses",
    analyzer: "Quadrupole or triple quadrupole", detector: "Electron multiplier",
    use: "Macromolecular organics, kerogen, meteorites", freq: "Medium" },
  { id: "GC-TOF", name: "GC-TOF-MS", family: "GC-MS",
    intro: "GC separation", ion: "Electron ionization (EI)", optics: "Ion lenses + reflectron",
    analyzer: "Time-of-flight", detector: "Microchannel plate",
    use: "Non-targeted organics, fast acquisition", freq: "Medium" },
  { id: "TD-GC-MS", name: "TD-GC-MS", family: "GC-MS",
    intro: "Thermal desorption + GC separation", ion: "Electron ionization (EI)", optics: "Ion lenses",
    analyzer: "Quadrupole", detector: "Electron multiplier",
    use: "Volatile organics, atmospheric chemistry", freq: "Medium" },

  // RIMS
  { id: "RIMS", name: "RIMS (Resonance Ionization MS)", family: "RIMS",
    intro: "Ion sputtering or thermal desorption of neutrals", ion: "Resonance ionization (tunable lasers)", optics: "Pulsed extraction + ion lenses",
    analyzer: "Time-of-flight", detector: "Microchannel plate / electron multiplier",
    use: "Isobar-free trace isotope analysis of stardust", freq: "Very Low" },
  { id: "LA-RIMS", name: "LA-RIMS", family: "RIMS",
    intro: "Laser ablation of neutrals", ion: "Resonance ionization (tunable lasers)", optics: "Pulsed extraction + ion lenses",
    analyzer: "Time-of-flight", detector: "Microchannel plate / electron multiplier",
    use: "In situ Rb-Sr dating, planetary science", freq: "Very Low" },

  // Other
  { id: "AMS", name: "Accelerator Mass Spectrometry", family: "AMS",
    intro: "Ion source (Cs sputter)", ion: "Cs sputter → negative ions → tandem accelerator (stripping)", optics: "Magnetic + electrostatic analysis (pre and post acceleration)",
    analyzer: "Magnetic sector + velocity filter + ΔE-E detector", detector: "Gas ionization detector / silicon detector",
    use: "Cosmogenic nuclides (¹⁴C, ¹⁰Be, ²⁶Al, ³⁶Cl)", freq: "Medium" },
  { id: "FT-ICR-MS", name: "FT-ICR-MS", family: "Other",
    intro: "ESI / MALDI / APCI", ion: "Electrospray / MALDI / APCI", optics: "Ion guides + multipole transfer",
    analyzer: "Penning trap (FT-ICR, superconducting magnet)", detector: "Image current detection (non-destructive)",
    use: "Ultra-high resolution organic/molecular analysis", freq: "Low" },
  { id: "Orbitrap", name: "Orbitrap MS", family: "Other",
    intro: "ESI / APCI + LC", ion: "Electrospray / APCI", optics: "Ion guides + C-trap",
    analyzer: "Orbitrap (electrostatic trap)", detector: "Image current detection (non-destructive)",
    use: "High-resolution molecular/organic analysis", freq: "Low" },
  { id: "GD-MS", name: "Glow Discharge MS", family: "Other",
    intro: "Direct solid sample (cathode)", ion: "Glow discharge (Ar plasma sputtering)", optics: "Ion lenses",
    analyzer: "Double-focusing magnetic sector or quadrupole", detector: "Faraday cup / electron multiplier",
    use: "Bulk trace elements in metals, semiconductors", freq: "Low" },
  { id: "SNMS", name: "Secondary Neutral MS", family: "Other",
    intro: "Ion sputtering (neutrals collected)", ion: "Post-ionization (electron beam or plasma)", optics: "Ion lenses",
    analyzer: "Quadrupole or TOF", detector: "Electron multiplier",
    use: "Quantitative surface/depth analysis, reduced matrix effects", freq: "Very Low" },
  { id: "APT", name: "Atom Probe Tomography", family: "Other",
    intro: "Field evaporation from needle-shaped specimen", ion: "Field ionization (high voltage pulse or laser)", optics: "No conventional optics (point projection)",
    analyzer: "Time-of-flight (point projection)", detector: "Position-sensitive detector (delay-line)",
    use: "3D atomic-scale composition mapping", freq: "Low" },
];

// Frequency ranking
const FREQ_ORDER = { "Very High": 5, "High": 4, "Medium": 3, "Low-Medium": 2.5, "Low": 2, "Very Low": 1 };
const FREQ_COLORS = {
  "Very High": "#1a7a3a", "High": "#2d9e4e", "Medium": "#d4a017",
  "Low-Medium": "#c4760c", "Low": "#b85c2f", "Very Low": "#8a3838"
};

// Component categorization
function categorize(field, value) {
  const v = value.toLowerCase();
  const cats = {
    intro: {
      "Solution nebulization": v.includes("solution") || v.includes("nebuliz"),
      "Laser ablation": v.includes("laser ablation"),
      "Filament loading": v.includes("filament"),
      "Ion sputtering": v.includes("sputter") || v.includes("primary ion"),
      "GC separation": v.includes("gc sep") || v.includes("gc ") && !v.includes("gas bench"),
      "Pyrolysis + GC": v.includes("pyrolysis"),
      "Thermal desorption + GC": v.includes("thermal desorption"),
      "Gas extraction / inlet": v.includes("vacuum extract") || v.includes("gas bench") || v.includes("gas intro") || v.includes("dual inlet") || v.includes("elemental analy") || v.includes("laser/furnace"),
      "Electrospray / MALDI": v.includes("esi") || v.includes("maldi") || v.includes("electrospray") || v.includes("apci"),
      "Field evaporation": v.includes("field evap"),
      "Direct solid": v.includes("direct solid") || v.includes("cathode"),
    },
    ion: {
      "Inductively Coupled Plasma": v.includes("inductively") || v.includes("icp"),
      "Thermal ionization": v.includes("thermal ion"),
      "Ion sputtering (secondary)": v.includes("ion sputtering") || v.includes("secondary"),
      "Electron ionization": v.includes("electron ion") || v.includes("nier"),
      "Resonance ionization": v.includes("resonance"),
      "Electrospray / MALDI": v.includes("electrospray") || v.includes("maldi") || v.includes("apci"),
      "Glow discharge": v.includes("glow"),
      "Field ionization": v.includes("field ion"),
      "Post-ionization": v.includes("post-ion"),
      "Optical (non-MS)": v.includes("optical") || v.includes("none"),
      "Accelerator stripping": v.includes("accelerat") || v.includes("stripping"),
    },
    analyzer: {
      "Quadrupole": (v.includes("quadrupole") && !v.includes("triple")) || v === "quadrupole",
      "Triple quadrupole": v.includes("triple"),
      "Magnetic sector (single)": v.includes("magnetic sector") && v.includes("single"),
      "Magnetic sector (double-focusing)": v.includes("double-focusing") || (v.includes("magnetic sector") && !v.includes("single") && !v.includes("time") && !v.includes("velocity")),
      "Time-of-flight": v.includes("time-of-flight") || v.includes("tof"),
      "FT-ICR (Penning trap)": v.includes("penning") || v.includes("ft-icr"),
      "Orbitrap": v.includes("orbitrap"),
      "Magnetic + velocity filter": v.includes("velocity"),
      "Point projection TOF": v.includes("point projection"),
      "Laser wavelength scanning": v.includes("laser wavelength") || v.includes("n/a"),
    },
    detector: {
      "Electron multiplier": v.includes("electron multiplier") && !v.includes("faraday") && !v.includes("array"),
      "Faraday cup(s)": v.includes("faraday") && !v.includes("electron") && !v.includes("ion counter"),
      "Faraday + EM": (v.includes("faraday") && v.includes("electron")) || (v.includes("faraday") && v.includes("ion counter")),
      "Faraday array (multi-collector)": v.includes("faraday cup array") && !v.includes("electron") && !v.includes("ion"),
      "EM array (multi-collector)": v.includes("electron multiplier array") || v.includes("5–7"),
      "Microchannel plate": v.includes("microchannel") && !v.includes("electron mult"),
      "MCP + EM": v.includes("microchannel") && v.includes("electron"),
      "Image current": v.includes("image current"),
      "Photodetector": v.includes("photodetect"),
      "Position-sensitive": v.includes("position-sensitive") || v.includes("delay-line"),
      "Gas ionization / Si": v.includes("gas ionization") || v.includes("silicon det"),
    }
  };
  return cats[field] || {};
}

function FreqDist({ field, systems }) {
  const counts = {};
  systems.forEach(s => {
    const val = s[field];
    const matches = categorize(field, val);
    Object.entries(matches).forEach(([cat, matched]) => {
      if (matched) counts[cat] = (counts[cat] || 0) + 1;
    });
  });
  const sorted = Object.entries(counts).sort((a,b) => b[1] - a[1]);
  const max = sorted.length > 0 ? sorted[0][1] : 1;
  return (
    <div style={{marginBottom: 16}}>
      {sorted.map(([cat, count]) => (
        <div key={cat} style={{display:"flex", alignItems:"center", marginBottom: 4, fontSize: 13}}>
          <span style={{width: 220, textAlign:"right", paddingRight: 8, color: "#555", flexShrink: 0}}>{cat}</span>
          <div style={{width: `${(count/max)*100}%`, minWidth: 2, background: "var(--bar-color, #4a7a9b)", height: 18, borderRadius: 3, display:"flex", alignItems:"center", paddingLeft: 6, transition: "width 0.3s"}}>
            <span style={{color: "#fff", fontSize: 11, fontWeight: 600}}>{count}</span>
          </div>
        </div>
      ))}
    </div>
  );
}

const FAMILIES = [...new Set(MS_SYSTEMS.map(s => s.family))];
const FAMILY_COLORS = {
  "ICP-MS": "#2563eb", "TIMS": "#7c3aed", "SIMS": "#db2777",
  "IRMS": "#059669", "Noble Gas": "#d97706", "GC-MS": "#dc2626",
  "RIMS": "#6366f1", "AMS": "#0891b2", "Other": "#6b7280"
};

export default function App() {
  const [selectedFamily, setSelectedFamily] = useState(null);
  const [selectedSystem, setSelectedSystem] = useState(null);
  const [viewMode, setViewMode] = useState("inventory");

  const filtered = selectedFamily
    ? MS_SYSTEMS.filter(s => s.family === selectedFamily)
    : MS_SYSTEMS;

  const familyCounts = useMemo(() => {
    const c = {};
    FAMILIES.forEach(f => { c[f] = MS_SYSTEMS.filter(s => s.family === f).length; });
    return c;
  }, []);

  return (
    <div style={{fontFamily: "'Inter', -apple-system, sans-serif", maxWidth: 1100, margin: "0 auto", padding: "20px 16px", color: "#1a1a1a"}}>
      <h1 style={{fontSize: 22, fontWeight: 700, marginBottom: 4}}>
        Earth Science Mass Spectrometer Systems Inventory
      </h1>
      <p style={{fontSize: 13, color: "#666", marginBottom: 20}}>
        {MS_SYSTEMS.length} system configurations across {FAMILIES.length} instrument families, mapped to 5 functional components
      </p>

      {/* View toggle */}
      <div style={{display: "flex", gap: 8, marginBottom: 16}}>
        {[["inventory", "System Inventory"], ["frequency", "Component Frequencies"]].map(([mode, label]) => (
          <button key={mode} onClick={() => setViewMode(mode)}
            style={{padding: "6px 14px", fontSize: 13, border: "1px solid #ccc", borderRadius: 4,
              background: viewMode === mode ? "#1a1a1a" : "#fff", color: viewMode === mode ? "#fff" : "#333",
              cursor: "pointer", fontWeight: viewMode === mode ? 600 : 400}}>
            {label}
          </button>
        ))}
      </div>

      {/* Family filter chips */}
      <div style={{display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 20}}>
        <button onClick={() => {setSelectedFamily(null); setSelectedSystem(null);}}
          style={{padding: "4px 10px", fontSize: 12, borderRadius: 12, cursor: "pointer",
            border: `1px solid ${!selectedFamily ? "#1a1a1a" : "#ccc"}`,
            background: !selectedFamily ? "#1a1a1a" : "#fff",
            color: !selectedFamily ? "#fff" : "#555", fontWeight: !selectedFamily ? 600 : 400}}>
          All ({MS_SYSTEMS.length})
        </button>
        {FAMILIES.map(f => (
          <button key={f} onClick={() => {setSelectedFamily(f); setSelectedSystem(null);}}
            style={{padding: "4px 10px", fontSize: 12, borderRadius: 12, cursor: "pointer",
              border: `1px solid ${selectedFamily === f ? FAMILY_COLORS[f] : "#ccc"}`,
              background: selectedFamily === f ? FAMILY_COLORS[f] : "#fff",
              color: selectedFamily === f ? "#fff" : "#555", fontWeight: selectedFamily === f ? 600 : 400}}>
            {f} ({familyCounts[f]})
          </button>
        ))}
      </div>

      {viewMode === "frequency" ? (
        <div>
          {[
            ["intro", "1. Sample Introduction", "#3b6e8f"],
            ["ion", "2. Ion Source / Ionization", "#6b3fa0"],
            ["analyzer", "3. Mass Analyzer", "#b85c2f"],
            ["detector", "4. Detector", "#2d7d4f"],
          ].map(([field, title, color]) => (
            <div key={field} style={{marginBottom: 24}}>
              <h3 style={{fontSize: 15, fontWeight: 600, marginBottom: 8, color}}>{title}</h3>
              <div style={{"--bar-color": color}}>
                <FreqDist field={field} systems={filtered} />
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div>
          {/* Table */}
          <div style={{overflowX: "auto"}}>
            <table style={{width: "100%", borderCollapse: "collapse", fontSize: 12}}>
              <thead>
                <tr style={{background: "#f5f5f5"}}>
                  {["System", "Freq.", "1. Sample Introduction", "2. Ion Source", "3. Mass Analyzer", "4. Detector", "Primary Use"].map(h => (
                    <th key={h} style={{padding: "8px 6px", textAlign: "left", borderBottom: "2px solid #ddd", fontSize: 11, fontWeight: 600, color: "#444"}}>{h}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {filtered.map((s, i) => (
                  <tr key={s.id}
                    onClick={() => setSelectedSystem(selectedSystem?.id === s.id ? null : s)}
                    style={{background: selectedSystem?.id === s.id ? "#eef3ff" : i % 2 === 0 ? "#fff" : "#fafafa",
                      cursor: "pointer", borderBottom: "1px solid #eee"}}>
                    <td style={{padding: "6px", fontWeight: 500}}>
                      <span style={{display:"inline-block", width: 8, height: 8, borderRadius: "50%",
                        background: FAMILY_COLORS[s.family], marginRight: 6}} />
                      {s.name}
                    </td>
                    <td style={{padding: "6px"}}>
                      <span style={{fontSize: 10, padding: "2px 6px", borderRadius: 8,
                        background: FREQ_COLORS[s.freq] + "18", color: FREQ_COLORS[s.freq], fontWeight: 600}}>
                        {s.freq}
                      </span>
                    </td>
                    <td style={{padding: "6px", color: "#555"}}>{s.intro}</td>
                    <td style={{padding: "6px", color: "#555"}}>{s.ion}</td>
                    <td style={{padding: "6px", color: "#555"}}>{s.analyzer}</td>
                    <td style={{padding: "6px", color: "#555"}}>{s.detector}</td>
                    <td style={{padding: "6px", color: "#777", fontStyle: "italic"}}>{s.use}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          {/* Detail panel */}
          {selectedSystem && (
            <div style={{marginTop: 16, padding: 16, background: "#f8f9fb", borderRadius: 8, border: "1px solid #e0e4ea"}}>
              <div style={{display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12}}>
                <h3 style={{fontSize: 16, fontWeight: 600, margin: 0}}>
                  <span style={{display:"inline-block", width: 10, height: 10, borderRadius: "50%",
                    background: FAMILY_COLORS[selectedSystem.family], marginRight: 8}} />
                  {selectedSystem.name}
                </h3>
                <span style={{fontSize: 11, padding: "3px 8px", borderRadius: 8,
                  background: FREQ_COLORS[selectedSystem.freq], color: "#fff", fontWeight: 600}}>
                  {selectedSystem.freq} usage
                </span>
              </div>
              <div style={{display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8}}>
                {[
                  ["1. Sample Introduction", selectedSystem.intro, "#3b6e8f"],
                  ["2. Ion Source", selectedSystem.ion, "#6b3fa0"],
                  ["3. Ion Optics / Transfer", selectedSystem.optics, "#8b5e3c"],
                  ["4. Mass Analyzer", selectedSystem.analyzer, "#b85c2f"],
                  ["5. Detector", selectedSystem.detector, "#2d7d4f"],
                ].map(([label, val, color]) => (
                  <div key={label} style={{padding: "8px 10px", background: "#fff", borderRadius: 6, borderLeft: `3px solid ${color}`}}>
                    <div style={{fontSize: 10, fontWeight: 600, color, marginBottom: 2}}>{label}</div>
                    <div style={{fontSize: 12}}>{val}</div>
                  </div>
                ))}
                <div style={{padding: "8px 10px", background: "#fff", borderRadius: 6, borderLeft: "3px solid #666"}}>
                  <div style={{fontSize: 10, fontWeight: 600, color: "#666", marginBottom: 2}}>Primary Application</div>
                  <div style={{fontSize: 12}}>{selectedSystem.use}</div>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      <div style={{marginTop: 24, padding: 12, background: "#f0f0f0", borderRadius: 6, fontSize: 11, color: "#666"}}>
        <strong>Note:</strong> Frequency ratings are qualitative estimates of prevalence in Earth/environmental science labs worldwide (Very High = nearly every analytical lab; Very Low = fewer than 10 instruments globally). CRDS is included as a non-MS isotope technique that has substantially replaced IRMS for water isotopes. Ion optics/transfer (component 3) is shown in the detail panel but omitted from the main table for space.
      </div>
    </div>
  );
}
