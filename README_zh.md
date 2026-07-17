# Restaurant Review System

🌐 **Language**

* 🇹🇼 繁體中文（目前）
* 🇺🇸 [English](README.md)

---

## 專案介紹

Restaurant Review System 是一個使用 **Django** 開發的餐廳評論網站，使用者可以瀏覽餐廳資訊、查看菜單，並登入後留下評論。

---

## 功能

* 使用者註冊
* 使用者登入／登出
* 瀏覽餐廳列表
* 查看餐廳詳細資訊
* 查看餐點資訊
* 發表評論
* 使用 Django Authentication 進行登入驗證
* 使用 Django Permission 控制評論權限
* 採用 Class-Based Views (CBVs)

---

## 技術

* Python 3.12
* Django 5.x
* SQLite
* Bootstrap
* HTML
* CSS

---

## 專案架構

```text
restaurant/
│
├── manage.py
├── restaurant/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── menu/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── permissions.py
    ├── templates/
    └── migrations/
```

---

## 資料庫設計

```text
Restaurant
│
├── Food
│
└── Comment
```

### Restaurant

* 餐廳名稱
* 電話
* 地址

### Food

* 餐點名稱
* 價格
* 備註
* 是否辣

### Comment

* 留言者
* Email
* 留言內容
* 建立時間

---

## 安裝方式

複製專案

```bash
git clone https://github.com/<your_username>/restaurant-review.git
```

建立虛擬環境

```bash
python -m venv venv
```

安裝套件

```bash
pip install -r requirements.txt
```

執行資料庫 Migration

```bash
python manage.py migrate
```

建立管理員（可選）

```bash
python manage.py createsuperuser
```

啟動專案

```bash
python manage.py runserver
```

瀏覽器開啟：

```text
http://127.0.0.1:8000/
```

---

## 學習重點

本專案涵蓋以下 Django 核心功能：

* Django Models
* ForeignKey 關聯
* Django ORM
* Generic Class-Based Views
* Django Forms
* Authentication
* Authorization
* URL Routing
* Template Rendering
* CRUD 操作

---

## 未來規劃

* 搜尋餐廳
* 評分系統
* 分頁功能
* 上傳餐廳圖片
* Django REST Framework API
* Docker
* 單元測試
* GitHub Actions CI/CD

---

## 專案遷移紀錄

此專案原始程式碼使用舊版 Django 撰寫，後續已完成升級至 Django 5.x。

主要修改內容包括：

* `url()` 改為 `path()`
* 使用 `LoginView`、`LogoutView`
* 所有 ForeignKey 新增 `on_delete`
* 更新 Template API
* 更新 Authentication API
* 調整專案結構符合新版 Django

---

## 授權

本專案僅供學習與教育用途。
