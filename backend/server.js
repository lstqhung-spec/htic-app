const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
const DATA_DIR = path.join(__dirname, 'data');
const ARTICLES_FILE = path.join(DATA_DIR, 'articles.json');
const CONTACTS_FILE = path.join(DATA_DIR, 'contacts.json');
const ADMINS_FILE = path.join(DATA_DIR, 'admins.json');
const FRONTEND_DIR = path.join(__dirname, '..', 'frontend');

// === TU DONG TAO DATABASE NEU CHUA CO ===

function initDatabase() {
    // Tao thu muc data neu chua co
    if (!fs.existsSync(DATA_DIR)) {
        fs.mkdirSync(DATA_DIR, { recursive: true });
        console.log('Da tao thu muc data/');
    }

    // Tao file articles.json neu chua co
    if (!fs.existsSync(ARTICLES_FILE)) {
        const articles = {
            articles: [
                {
                    id: 1,
                    title: 'Luat Doanh nghiep 2020 - Nhung diem moi quan trong',
                    content: 'Luat Doanh nghiep so 59/2020/QH14 co hieu luc tu ngay 01/01/2021, thay the Luat Doanh nghiep 2014.',
                    created_at: '2025-01-15'
                },
                {
                    id: 2,
                    title: 'Quy dinh moi ve thue TNCN nam 2025',
                    content: 'Muc giam tru gia canh cho nguoi nop thue la 11 trieu dong/thang va 4,4 trieu dong/thang cho moi nguoi phu thuoc.',
                    created_at: '2025-01-14'
                },
                {
                    id: 3,
                    title: 'Huong dan dang ky BHXH cho doanh nghiep moi',
                    content: 'Doanh nghiep moi thanh lap phai dang ky tham gia BHXH trong vong 30 ngay ke tu ngay ky hop dong lao dong dau tien.',
                    created_at: '2025-01-13'
                }
            ]
        };
        fs.writeFileSync(ARTICLES_FILE, JSON.stringify(articles, null, 2));
        console.log('Da tao file articles.json');
    }

    // Tao file contacts.json neu chua co
    if (!fs.existsSync(CONTACTS_FILE)) {
        const contacts = { contacts: [] };
        fs.writeFileSync(CONTACTS_FILE, JSON.stringify(contacts, null, 2));
        console.log('Da tao file contacts.json');
    }

    // Tao file admins.json neu chua co
    if (!fs.existsSync(ADMINS_FILE)) {
        const admins = {
            admins: [
                {
                    id: 1,
                    username: 'admin',
                    password: 'htic2025',
                    name: 'Administrator'
                }
            ]
        };
        fs.writeFileSync(ADMINS_FILE, JSON.stringify(admins, null, 2));
        console.log('Da tao file admins.json');
    }

    console.log('Database san sang!');
}

// === DOC/GHI FILE JSON ===

function readJSON(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        return JSON.parse(content);
    } catch (error) {
        return null;
    }
}

function writeJSON(filePath, data) {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
}

// === CAC HAM XU LY ARTICLES ===

function getAllArticles() {
    const data = readJSON(ARTICLES_FILE);
    return data ? data.articles : [];
}

function getArticleById(id) {
    const articles = getAllArticles();
    return articles.find(a => a.id === id);
}

function createArticle(title, content) {
    const data = readJSON(ARTICLES_FILE);
    const maxId = data.articles.length > 0 ? Math.max(...data.articles.map(a => a.id)) : 0;
    const newArticle = {
        id: maxId + 1,
        title: title,
        content: content,
        created_at: new Date().toISOString().split('T')[0]
    };
    data.articles.push(newArticle);
    writeJSON(ARTICLES_FILE, data);
    return newArticle.id;
}

function updateArticle(id, title, content) {
    const data = readJSON(ARTICLES_FILE);
    const index = data.articles.findIndex(a => a.id === id);
    if (index !== -1) {
        data.articles[index].title = title;
        data.articles[index].content = content;
        writeJSON(ARTICLES_FILE, data);
        return true;
    }
    return false;
}

function deleteArticle(id) {
    const data = readJSON(ARTICLES_FILE);
    const index = data.articles.findIndex(a => a.id === id);
    if (index !== -1) {
        data.articles.splice(index, 1);
        writeJSON(ARTICLES_FILE, data);
        return true;
    }
    return false;
}

// === CAC HAM XU LY CONTACTS ===

function getAllContacts() {
    const data = readJSON(CONTACTS_FILE);
    return data ? data.contacts : [];
}

function createContact(name, phone, email, message) {
    const data = readJSON(CONTACTS_FILE);
    const maxId = data.contacts.length > 0 ? Math.max(...data.contacts.map(c => c.id)) : 0;
    const newContact = {
        id: maxId + 1,
        name: name,
        phone: phone,
        email: email,
        message: message,
        created_at: new Date().toISOString().split('T')[0]
    };
    data.contacts.push(newContact);
    writeJSON(CONTACTS_FILE, data);
    return newContact.id;
}

function deleteContact(id) {
    const data = readJSON(CONTACTS_FILE);
    const index = data.contacts.findIndex(c => c.id === id);
    if (index !== -1) {
        data.contacts.splice(index, 1);
        writeJSON(CONTACTS_FILE, data);
        return true;
    }
    return false;
}

// === KIEM TRA DANG NHAP ===

function checkAdminLogin(username, password) {
    const data = readJSON(ADMINS_FILE);
    if (data) {
        return data.admins.find(a => a.username === username && a.password === password);
    }
    return null;
}

// === XU LY BODY REQUEST ===

function getBody(req) {
    return new Promise((resolve) => {
        let body = '';
        req.on('data', chunk => body += chunk);
        req.on('end', () => {
            try {
                resolve(JSON.parse(body));
            } catch (e) {
                resolve({});
            }
        });
    });
}

// === TAO SERVER ===

const server = http.createServer(async (req, res) => {
    const url = req.url;
    const method = req.method;
    
    console.log(`[${new Date().toLocaleTimeString()}] ${method} ${url}`);
    
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }

    // === API CONG KHAI ===

    if (url === '/api/articles' && method === 'GET') {
        const articles = getAllArticles();
        res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify(articles));
        return;
    }

    if (url === '/api/contacts' && method === 'POST') {
        const body = await getBody(req);
        const id = createContact(body.name, body.phone, body.email || '', body.message);
        console.log(`   => Lien he moi tu: ${body.name} (ID: ${id})`);
        res.writeHead(201, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ success: true, message: 'Cam on ban da gui thong tin!' }));
        return;
    }

    // === API ADMIN ===

    if (url === '/api/admin/login' && method === 'POST') {
        const body = await getBody(req);
        const admin = checkAdminLogin(body.username, body.password);
        if (admin) {
            console.log(`   => Admin dang nhap: ${admin.name}`);
            res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ success: true, name: admin.name }));
        } else {
            res.writeHead(401, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ success: false, message: 'Sai thong tin' }));
        }
        return;
    }

    if (url.match(/^\/api\/admin\/articles\/\d+$/) && method === 'GET') {
        const id = parseInt(url.split('/')[4]);
        const article = getArticleById(id);
        if (article) {
            res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify(article));
        } else {
            res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ error: 'Khong tim thay' }));
        }
        return;
    }

    if (url === '/api/admin/articles' && method === 'POST') {
        const body = await getBody(req);
        const id = createArticle(body.title, body.content);
        console.log(`   => Them bai viet: "${body.title}" (ID: ${id})`);
        res.writeHead(201, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ success: true, id: id }));
        return;
    }

    if (url.match(/^\/api\/admin\/articles\/\d+$/) && method === 'PUT') {
        const id = parseInt(url.split('/')[4]);
        const body = await getBody(req);
        const success = updateArticle(id, body.title, body.content);
        if (success) {
            console.log(`   => Cap nhat bai viet ID: ${id}`);
            res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ success: true }));
        } else {
            res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ error: 'Khong tim thay' }));
        }
        return;
    }

    if (url.match(/^\/api\/admin\/articles\/\d+$/) && method === 'DELETE') {
        const id = parseInt(url.split('/')[4]);
        const success = deleteArticle(id);
        if (success) {
            console.log(`   => Xoa bai viet ID: ${id}`);
            res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ success: true }));
        } else {
            res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ error: 'Khong tim thay' }));
        }
        return;
    }

    if (url === '/api/admin/contacts' && method === 'GET') {
        const contacts = getAllContacts();
        res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify(contacts));
        return;
    }

    if (url.match(/^\/api\/admin\/contacts\/\d+$/) && method === 'DELETE') {
        const id = parseInt(url.split('/')[4]);
        const success = deleteContact(id);
        if (success) {
            console.log(`   => Xoa lien he ID: ${id}`);
            res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ success: true }));
        } else {
            res.writeHead(404, { 'Content-Type': 'application/json; charset=utf-8' });
            res.end(JSON.stringify({ error: 'Khong tim thay' }));
        }
        return;
    }

    // === PHUC VU FILE HTML ===

    if (url === '/' || url === '/index.html') {
        const filePath = path.join(FRONTEND_DIR, 'index.html');
        if (fs.existsSync(filePath)) {
            res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            res.end(fs.readFileSync(filePath, 'utf8'));
        } else {
            res.writeHead(404);
            res.end('Khong tim thay file index.html');
        }
        return;
    }

    if (url === '/admin' || url === '/admin.html') {
        const filePath = path.join(FRONTEND_DIR, 'admin.html');
        if (fs.existsSync(filePath)) {
            res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            res.end(fs.readFileSync(filePath, 'utf8'));
        } else {
            res.writeHead(404);
            res.end('Khong tim thay file admin.html');
        }
        return;
    }

    res.writeHead(404);
    res.end('404 - Trang khong ton tai');
});

// === KHOI DONG ===

// Tu dong tao database neu chua co
initDatabase();

server.listen(PORT, () => {
    console.log('');
    console.log('==============================================');
    console.log('   HTIC LEGAL APP - JSON DATABASE');
    console.log('==============================================');
    console.log('');
    console.log('   Server dang chay tren port: ' + PORT);
    console.log('');
    console.log('   Tai khoan: admin / htic2025');
    console.log('');
    console.log('==============================================');
    console.log('');
});
