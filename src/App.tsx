import { Activity, Database, Gauge, Route } from 'lucide-react';
import { MetricCard } from './components/MetricCard';
import { RoutingTable } from './components/RoutingTable';

const metrics = {
  totalRequests: 12842,
  cacheHitRate: '71.4%',
  averageLatency: '84 ms',
  activeRules: 2,
};

const rules = [
  { name: 'code-prompts', matchType: 'keyword', target: 'codellama', priority: 100, status: 'Active' },
  { name: 'general-prompts', matchType: 'fallback', target: 'llama3.1', priority: 10, status: 'Active' },
];

function App() {
  return (
    <main className="min-h-screen bg-slate-50 text-ink">
      <header className="border-b border-line bg-white">
        <div className="mx-auto flex max-w-7xl flex-col gap-4 px-6 py-6 md:flex-row md:items-center md:justify-between">
          <div>
            <h1 className="text-2xl font-semibold tracking-normal">Legion LLM Gateway</h1>
            <p className="mt-1 text-sm text-steel">
              Semantic cache, model routing, and request telemetry for local inference.
            </p>
          </div>
          <div className="flex items-center gap-2 rounded border border-line bg-slate-50 px-3 py-2 text-sm text-steel">
            <Database size={16} aria-hidden="true" />
            MariaDB-ready persistence
          </div>
        </div>
      </header>

      <section className="mx-auto max-w-7xl px-6 py-6">
        <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          <MetricCard icon={Activity} label="Total requests" value={metrics.totalRequests.toLocaleString()} />
          <MetricCard icon={Gauge} label="Cache hit rate" value={metrics.cacheHitRate} />
          <MetricCard icon={Activity} label="Average latency" value={metrics.averageLatency} />
          <MetricCard icon={Route} label="Active routing rules" value={String(metrics.activeRules)} />
        </div>

        <div className="mt-6 grid gap-6 lg:grid-cols-[1fr_360px]">
          <RoutingTable rules={rules} />
          <aside className="rounded border border-line bg-white p-5">
            <h2 className="text-base font-semibold">Gateway status</h2>
            <dl className="mt-4 space-y-3 text-sm">
              <div className="flex justify-between gap-4">
                <dt className="text-steel">Ollama upstream</dt>
                <dd className="font-medium text-success">Optional</dd>
              </div>
              <div className="flex justify-between gap-4">
                <dt className="text-steel">Fallback mode</dt>
                <dd className="font-medium">Deterministic</dd>
              </div>
              <div className="flex justify-between gap-4">
                <dt className="text-steel">Cache policy</dt>
                <dd className="font-medium">Cosine threshold</dd>
              </div>
              <div className="flex justify-between gap-4">
                <dt className="text-steel">API surface</dt>
                <dd className="font-medium">FastAPI</dd>
              </div>
            </dl>
          </aside>
        </div>
      </section>
    </main>
  );
}

export default App;
