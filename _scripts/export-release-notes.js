const { join } = require('path')
const { writeFileSync } = require('fs')

const sanitize = require('sanitize-filename')
const c = require('centra')

const USER_AGENT = 'ReleaseScrapperBot/1.0 (+https://github.com/sfztools/sfztools.github.io)'
const REPO_NAME = 'sfztools/sfizz'
const DIR = '_posts'

const dateStr = date => date.getFullYear().toString()
  + '-'
  + (date.getMonth() + 1).toString().padStart(2, '0')
  + '-'
  + date.getDate().toString().padStart(2, '0')

const json = url => c(url)
  .header('User-Agent', USER_AGENT)
  .header('Application-Type', 'application/vnd.github.v3+json')
  .send()
  .then(r => r.json())

const assetLink = asset => {
  return `- [${asset.name}](${asset.browser_download_url})`;
}
const articleName = (name, date) => `${dateStr(new Date(date))}-sfizz-${name}-release.md`

const makeArticle = release => `
---
title: "sfizz ${release.name} release"
author: "${release.author.login}"
date: "${new Date(release.published_at).toISOString()}"
---
${release.body.replaceAll('\r\n', '\n')}

See: [GitHub release page](${release.html_url})

##### Download links:
${release.assets.map(assetLink).join('\n') || '- None'}
`.trim()

async function main() {
  const releases = await json(`https://api.github.com/repos/${REPO_NAME}/releases`)
  const exported = releases
    .map(makeArticle)
    .map((article, i)=> [ article, sanitize(articleName(releases[i].name, releases[i].published_at)) ])
    .map(([article, name]) => writeFileSync(join(DIR, name), article))

  console.log(`Exported ${exported.length} release note(s)`)
}
main()
