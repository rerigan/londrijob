const isProd = process.env.NODE_ENV === 'production';

const nextConfig = {
  output: 'export', // necessário para exportação estática
  basePath: '/londrijob', // substitua pelo nome do seu repo
  assetPrefix: isProd ? '/londrijob/' : '',
};

module.exports = nextConfig;