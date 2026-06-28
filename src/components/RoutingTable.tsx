type Rule = {
  name: string;
  matchType: string;
  target: string;
  priority: number;
  status: string;
};

type RoutingTableProps = {
  rules: Rule[];
};

export function RoutingTable({ rules }: RoutingTableProps) {
  return (
    <section className="rounded border border-line bg-white">
      <div className="border-b border-line px-5 py-4">
        <h2 className="text-base font-semibold">Routing rules</h2>
      </div>
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-line text-sm">
          <thead className="bg-slate-50 text-left text-xs uppercase text-steel">
            <tr>
              <th className="px-5 py-3 font-semibold">Rule</th>
              <th className="px-5 py-3 font-semibold">Match</th>
              <th className="px-5 py-3 font-semibold">Target model</th>
              <th className="px-5 py-3 font-semibold">Priority</th>
              <th className="px-5 py-3 font-semibold">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-line">
            {rules.map((rule) => (
              <tr key={rule.name}>
                <td className="px-5 py-4 font-medium">{rule.name}</td>
                <td className="px-5 py-4 text-steel">{rule.matchType}</td>
                <td className="px-5 py-4 text-steel">{rule.target}</td>
                <td className="px-5 py-4 text-steel">{rule.priority}</td>
                <td className="px-5 py-4">
                  <span className="rounded border border-emerald-200 bg-emerald-50 px-2 py-1 text-xs font-medium text-success">
                    {rule.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
