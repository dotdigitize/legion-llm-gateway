import type { LucideIcon } from 'lucide-react';

type MetricCardProps = {
  icon: LucideIcon;
  label: string;
  value: string;
};

export function MetricCard({ icon: Icon, label, value }: MetricCardProps) {
  return (
    <article className="rounded border border-line bg-white p-5">
      <div className="flex items-center justify-between gap-3">
        <p className="text-sm font-medium text-steel">{label}</p>
        <Icon className="text-signal" size={18} aria-hidden="true" />
      </div>
      <p className="mt-3 text-3xl font-semibold tracking-normal">{value}</p>
    </article>
  );
}
